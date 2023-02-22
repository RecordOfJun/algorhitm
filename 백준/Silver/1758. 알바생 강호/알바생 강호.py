import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)
tip=0
for i in range(n):
    if(arr[i]-(i)>0):
        tip+=arr[i]-(i)

print(tip)