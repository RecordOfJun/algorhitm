import math
n,m=map(int,input().split(" "))
arr=set()
for i in range(m):
    a,b=map(int,input().split(" "))
    y=max(a,b)
    x=min(a,b)
    for j in range(1,n+1):
        if(j<x):
            arr.add((j,x,y))
        elif(j>x and j<y):
            arr.add((x,j,y))
        elif(j>y):
            arr.add((x,y,j))
maximum=math.comb(n,3)
print(maximum-len(arr))