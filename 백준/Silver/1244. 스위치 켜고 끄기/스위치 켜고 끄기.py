def male(arr,n,x):
    for i in range(x-1,n,x):
        if arr[i]==0:
            arr[i]=1
        else:
            arr[i]=0

def female(arr,n,x):
    i=x
    j=x
    while True:
        if i<0 or j>=n:
            break
        if arr[i]!=arr[j]:
            break
        i-=1
        j+=1
    
    for a in range(i+1,j):
        if arr[a]==0:
            arr[a]=1
        else:
            arr[a]=0

n=int(input())
arr=list(map(int,input().split(" ")))
m=int(input())
for i in range(m):
    a,b=map(int,input().split(" "))
    if a==1:
        male(arr,n,b)
    else:
        female(arr,n,b-1)

for i in range(n):
    print(arr[i],end=" ")
    if((i+1)%20==0):
        print()