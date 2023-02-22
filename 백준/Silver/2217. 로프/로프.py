import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

max=0
arr.sort()
for i in range(n):
    if(arr[i]*(n-i)>max):
        max=arr[i]*(n-i)

print(max)