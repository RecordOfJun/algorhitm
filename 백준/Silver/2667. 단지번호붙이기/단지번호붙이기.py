from collections import deque
from itertools import *
import sys
import math
def bfs(i,j,graph,graph_v,n):
    
    if graph_v[i][j]==True or graph[i][j]=="0":
        return 0
    
    queue=deque()
    queue.append((i,j))
    graph_v[i][j]=True
    cnt=1
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if(nx<0 or ny<0 or nx>=n or ny>=n):
                continue
            if(graph_v[nx][ny]==True or graph[nx][ny]=="0"):
                continue
            
            graph_v[nx][ny]=True
            cnt+=1
            queue.append((nx,ny))
    
    return cnt

n=int(input())
graph=[]
graph_v=[[False]*n for _ in range(n)]
arr=[]
for i in range(n):
    graph.append(input())

for i in range(n):
    for j in range(n):
        num=bfs(i,j,graph,graph_v,n)
        if(num!=0):
            arr.append(num)
arr.sort()
print(len(arr))
for case in arr:
    print(case)