import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
from collections import deque

n,m=map(int,input().split(" "))
arr=[]
cnt=[[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    arr.append(input())
queue=deque()
queue.append((0,0))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
while queue:
    x,y=queue.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx==n or nx==-1 or ny==m or ny==-1:
            continue
        if arr[nx][ny]=='0':
            continue
        if cnt[nx][ny]!=0:
            continue
        cnt[nx][ny]=cnt[x][y]+1
        queue.append((nx,ny))
print(cnt[n-1][m-1]+1)