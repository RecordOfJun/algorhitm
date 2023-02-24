import heapq
import sys

n=int(input())
heap=[]
for _ in range(n):
    heapq.heappush(heap,int(sys.stdin.readline().rstrip()))
cnt=0
if(len(heap)==1):
    print(0)
    exit()
while heap:
    a=heapq.heappop(heap)
    cnt+=a
    if(heap):
        b=heapq.heappop(heap)
        cnt+=b
        if(heap):
            heapq.heappush(heap,a+b)

print(cnt)
    