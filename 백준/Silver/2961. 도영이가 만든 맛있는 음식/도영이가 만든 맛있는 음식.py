import itertools

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))
min_num=1000000000
# for item in arr:
#     s =item[0]
#     b =item[1]
#     if abs(s - b) < min_num:
#         min_num = abs(s - b)
#     if min_num == 0:
#         print(0)
#         exit()
# if n>1:
for i in range(1,n+1):
    cases=list(itertools.combinations(arr,i))
    for case in cases:
        s=1
        b=0
        for item in case:
           s*=item[0]
           b+=item[1]
        if abs(s-b)<min_num:
            min_num=abs(s-b)
        if min_num==0:
            print(0)
            exit()
print(min_num)