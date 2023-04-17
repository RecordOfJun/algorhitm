from collections import deque
def bfs(n,v):
    arr_check=[0 for _ in range(n+1)]
    queue=deque()
    queue.append(v)
    arr_check[v]=1
    while queue:
        value=queue.popleft()
        print(value,end=" ")
        for item in arr[value]:
            if arr_check[item]==0:
                queue.append(item)
                arr_check[item]=1

def dfs(v):
    check_arr[v]=1
    print(v,end=" ")
    for item in arr[v]:
        if check_arr[item]==0:
            dfs(item)

n,m,v=map(int,input().split(" "))
arr=[[] for _ in range(n+1)]
check_arr=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split(" "))
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,n+1):
    if arr[i]:
        arr[i].sort()
dfs(v)
print()
bfs(n,v)