from collections import deque
n=int(input())
arr_check=[0 for _ in range(n+1)]
arr=[[] for _ in range(n+1)]
m=int(input())
for _ in range(m):
    a,b=map(int,input().split(" "))
    arr[a].append(b)
    arr[b].append(a)

queue=deque()
queue.append(1)
arr_check[1]=1
cnt=0
while queue:
    value=queue.popleft()
    for item in arr[value]:
        if arr_check[item]==0:
            queue.append(item)
            arr_check[item]=1
            cnt+=1
print(cnt)