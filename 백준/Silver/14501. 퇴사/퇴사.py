def func(arr,i,n,p,total_p):
    if i==n:
        total_p+=p
    if i>=n:
        return total_p
    total_p+=p
    return max(func(arr,i+arr[i][0],n,arr[i][1],total_p),func(arr,i+1,n,0,total_p))

n=int(input())
arr=[]
for i in range(n):
    t,p=map(int,input().split(" "))
    arr.append((t,p))

result=func(arr,0,n,0,0)
print(result)