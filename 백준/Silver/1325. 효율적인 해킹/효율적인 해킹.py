import sys
from collections import defaultdict
from collections import deque
def bfs(v,n):
    arr_check=[0 for _ in range(n+1)]
    queue=deque()
    queue.append(v)
    arr_check[v]=1
    cnt=0
    while queue:
        value=queue.popleft()
        for item in arr[value]:
            if arr_check[item]==0:
                cnt+=1
                arr_check[item]=1
                queue.append(item)
    return cnt
input=sys.stdin.readline
n,m=map(int,input().split(" "))
arr=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split(" "))
    arr[b].append(a)
max_arr=[]
max_value=-1
for i in range(1,n+1):
    value=bfs(i,n)
    if value>max_value:
        max_arr=[i]
        max_value=value
    elif value==max_value:
        max_arr.append(i)

for item in max_arr:
    print(item,end=" ")