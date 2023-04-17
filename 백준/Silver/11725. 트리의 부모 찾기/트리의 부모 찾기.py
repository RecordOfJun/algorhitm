import sys
from collections import defaultdict
from collections import deque
input=sys.stdin.readline
parent=defaultdict(int)
parent[1]=-11
n=int(input())
arr=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split(" "))
    arr[a].append(b)
    arr[b].append(a)
queue=deque()
queue.append(1)
while queue:
    value=queue.popleft()
    for item in arr[value]:
        if parent[item]==0:
            parent[item]=value
            queue.append(item)
for i in range(2,n+1):
    print(parent[i])