import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
from collections import deque

n,m=map(int,input().split(" "))
arr=[]
check_arr=[[0 for _ in range(m)]for _ in range(n)]
start=()
for i in range(n):
    l=list(map(int,input().split(" ")))
    if 2 in l:
        j=l.index(2)
        start=(i,j)
    arr.append(l)

queue=deque()
check_arr[start[0]][start[1]]=1
arr[start[0]][start[1]]=0
queue.append((start[0],start[1]))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while queue:
    x,y=queue.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx==n or nx==-1 or ny==m or ny==-1:
            continue
        if check_arr[nx][ny]!=0:
            continue
        if arr[nx][ny]==0:
            continue
        arr[nx][ny]=arr[x][y]+1
        queue.append((nx,ny))
        check_arr[nx][ny]=1

for i in range(n):
    for j in range(m):
        if check_arr[i][j]==0 and arr[i][j]!=0:
            print(-1,end=" ")
        else:
            print(arr[i][j],end=" ")
    print()