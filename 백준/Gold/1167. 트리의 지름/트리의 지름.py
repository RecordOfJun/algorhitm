import sys
from collections import deque
from itertools import *
import heapq
def get_distance(x,graph,n):
    graph_d=[ int(1e9) for _ in range(n+1)]
    graph_d[0]=-1
    graph_d[x]=0
    max_d=0
    max_idx=0
    heap=[]
    heap.append((x,graph[x]))
    while heap:
        values=heapq.heappop(heap)
        for value in values[1]:
            if(value[0]+graph_d[values[0]]<graph_d[value[1]]):
                graph_d[value[1]]=value[0]+graph_d[values[0]]
                if(graph_d[value[1]]>max_d):
                    max_d=graph_d[value[1]]
                    max_idx=value[1]
                heapq.heappush(heap,(value[1],graph[value[1]]))

    return (max_idx,max_d)


n=int(input())
graph=[[] for _ in range(n+1)]
lasts=[]
lasts_cnt=0
for i in range(n):
    arr=list(map(int,input().split(" ")))
    m=len(arr)
    for j in range(1,m-2,2):
        graph[arr[0]].append((arr[j+1],arr[j]))
    if(m==4):
        lasts.append(arr[0])
        lasts_cnt+=1
max_idx,max_d=get_distance(lasts[0],graph,n)
max_idx,max_d=get_distance(max_idx,graph,n)

print(max_d)