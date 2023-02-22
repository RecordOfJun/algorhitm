from collections import deque
import sys
n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split(" "))
    arr.append((a,b))

queue=deque(sorted(arr,key=lambda x:(x[1],x[0])))

last=0
cnt=0
for i in range(n):
    time=queue.popleft()
    if(time[0]>=last):
        cnt+=1
        last=time[1]
print(cnt)
