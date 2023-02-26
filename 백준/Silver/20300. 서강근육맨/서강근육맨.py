from collections import deque
n=int(input())
arr=list(map(int,input().split(" ")))
arr.sort()
queue=deque(arr)
M=0
if(n%2==1):
    M=queue.pop()

while queue:
    value=queue.pop()+queue.popleft()
    if value>M:
        M=value

print(M)