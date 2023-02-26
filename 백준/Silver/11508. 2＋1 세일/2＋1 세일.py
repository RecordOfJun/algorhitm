import sys
import heapq
n=int(input())
arr=[]
for i in range(n):
    heapq.heappush(arr,-int(sys.stdin.readline().rstrip()))

cnt=0
total=0
while arr:
    value=-heapq.heappop(arr)
    total+=value
    cnt+=1
    if(cnt==3):
        total-=value
        cnt=0

print(total)