import itertools
n,m=map(int,input().split(" "))
arr=[]
for i in range(n):
    arr.append(list((map(int,input().split(" ")))))

cases=list(itertools.combinations(range(m),3))

result=0
for case in cases:
    s=0
    for i in range(n):
        s+=max(arr[i][case[0]],arr[i][case[1]],arr[i][case[2]])
    result=max(result,s)

print(result)