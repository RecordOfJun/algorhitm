import sys
from collections import defaultdict
import heapq
n=int(input())
dict=defaultdict(list)
heap=[]
feed_arr=[[0]*n for _ in range(n)]
load_arr=[[1]*n for _ in range(n)]

for i in range(n):
    temp=list(map(int,sys.stdin.readline().rstrip().split(" ")))
    for j in range(n):
        dict[temp[j]].append((i,j))
        feed_arr[i][j]=temp[j]
        heap.append(-temp[j])

heap=list(set(heap))
heapq.heapify(heap)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

max_cnt=1
while heap:
    result=-heapq.heappop(heap)
    arr=dict[result]
    for item in arr:
        x=item[0]
        y=item[1]
        max_load=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(nx<0 or ny<0 or nx>=n or ny>=n):
                continue
            if(feed_arr[nx][ny]<=feed_arr[x][y]):
                continue
            value=load_arr[nx][ny]+1
            if(value>max_load):
                max_load=value
            load_arr[x][y]=max_load
            if(max_load>max_cnt):
                max_cnt=max_load

print(max_cnt)

