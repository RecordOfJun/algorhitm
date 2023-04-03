import itertools
n=int(input())
whole={i for i in range(n)}
arr=[[]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split(" ")))

cases=list(itertools.combinations(range(n),n//2))
case_len=len(cases)//2
min_num=10e+16
min_away=[]
min_home=[]
for i in range(case_len):
    home=cases[i]
    away=list(whole-set(home))
    home_cnt=0
    away_cnt=0
    for combi in list(itertools.permutations(home,2)):
        home_cnt+=arr[combi[0]][combi[1]]
    for combi in list(itertools.permutations(away,2)):
        away_cnt+=arr[combi[0]][combi[1]]
    sub=abs(home_cnt-away_cnt)
    if sub < min_num:
        min_num=sub
        min_home=home
        min_away=away

print(min_num)