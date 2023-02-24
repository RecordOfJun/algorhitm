from collections import deque
from itertools import *
import sys
import math
def bfs(x,graph,graph_d,k):
    queue=deque()
    queue.append(x)
    arr=[]
    while queue:
        idx=queue.popleft()
        for case in graph[idx]:
            if(graph_d[case]!=0 or case==x):
                continue
            if(graph_d[case]==0):
                graph_d[case]=graph_d[idx]+1
                queue.append(case)
            if(graph_d[case]==k):
                arr.append(case)
    return arr


n,m,k,x=map(int,input().split(" "))
graph=[[] for _ in range(n+1)]
graph_d=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().rstrip().split(" "))
    graph[a].append(b)

arr=bfs(x,graph,graph_d,k)
if(len(arr)==0):
    print(-1)

else:
    arr.sort()
    for case in arr:
        print(case)