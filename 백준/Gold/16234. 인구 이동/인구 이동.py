import sys
from collections import deque
input=sys.stdin.readline
iscontinue=[True]
def init_visited(isvisited,n):
    for i in range(n):
        for j in range(n):
            isvisited[i][j]=False

def bfs(arr,isvisited,queue,i,j,l,r):
    if isvisited[i][j]:
        return
    sum_list=[]
    total=0
    cnt=1
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    queue.append((i,j))
    isvisited[i][j]=True
    total += arr[i][j]
    sum_list.append((i, j))
    while queue:
        x,y=queue.popleft()
        value=arr[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==n or ny==n or nx==-1 or ny==-1:
                continue
            if isvisited[nx][ny]:
                continue
            if abs(arr[nx][ny]-value)>=l and abs(arr[nx][ny]-value)<=r:
                total+=arr[nx][ny]
                sum_list.append((nx,ny))
                isvisited[nx][ny]=True
                cnt+=1
                queue.append((nx,ny))
    if cnt!=1:
        avg=total//cnt
        for idx in sum_list:
            x,y=idx
            if avg!=arr[x][y]:
                iscontinue[0]=True
            arr[x][y]=avg



n,l,r=map(int,input().split(" "))
arr=[]
isvisited=[[False]*n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))

queue=deque()
total_cnt=-1
while iscontinue[0]:
    iscontinue[0]=False
    total_cnt+=1
    init_visited(isvisited,n)
    for i in range(n):
        for j in range(n):
            bfs(arr,isvisited,queue,i,j,l,r)

print(total_cnt)