import itertools
n=int(input())
whole={i for i in range(n)}
arr=[[]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split(" ")))
min_num=10e+16
num=n//2

for num in range(n//2,0,-1):
    cases=list(itertools.combinations(range(n),num))
    case_len=len(cases)
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
        if min_num==0:
            print(0)
            exit()

print(min_num)