from collections import deque
import sys
def bfs(x,y,graph,n,m):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    if(graph[x][y]==2):
        return False
    
    queue=deque()
    queue.append((x,y))
    graph[x][y]=2
    while queue:
        a,b=queue.popleft()

        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]

            if(na<0 or na>=n or nb<0 or nb>=m):
                continue
            if(graph[na][nb]!=1):
                continue
            else:
                graph[na][nb]=2
                queue.append((na,nb))
    return True


h=int(input())

for _ in range(h):
    m,n,a=map(int,input().split(" "))
    graph=[[0]*m for _ in range(n)]
    a_list=[]
    cnt=0
    for k in range(a):
        j,i=map(int,sys.stdin.readline().rstrip().split(" "))
        a_list.append((i,j))
        graph[i][j]=1
    for case in a_list:
        if bfs(case[0],case[1],graph,n,m):
            cnt+=1
    print(cnt)