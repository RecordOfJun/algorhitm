import sys
from collections import deque
import heapq
import math

def rotate(benchmark,point):
    x,y=benchmark
    sx,sy=point
    dy = x - y - sx
    dx = x + y - sy
    destination=(dx,-dy)
    return destination

def curve(arr,x,y,d,g):
    dir_x=[1,0,-1,0]
    dir_y=[0,-1,0,1]
    last=[x+dir_x[d],y+dir_y[d]]
    points=[]
    points.append((x,y))
    points.append((last[0],last[1]))
    cnt=0
    #포인트들을 끝점 기준으로 90도 돌린다음에 포인트 배열에 추가하고 끝점을 최신화해주기
    #두 점 주어졌을 때 90도 회전 어케함?-> 두 점이 주어졌을 때 이등변 직각삼각형 만들기
    while cnt<g:
        cnt+=1
        new_points = []
        for point in points:
            new_points.append(rotate(last,point))
        new_points.pop()
        while new_points:
            points.append(new_points.pop())

        lastx,lasty=points.pop()
        last=[lastx,lasty]
        points.append((lastx,lasty))
    for point in points:
        x,y=point
        arr[x][y]=1

def find(arr):
    cnt=0
    for i in range(100):
        for j in range(100):
            if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]==1 and arr[i+1][j+1]==1:
                cnt+=1
    return cnt

input=sys.stdin.readline
n=int(input())
arr=[[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x,y,d,g=map(int,input().split(" "))
    curve(arr,x,y,d,g)

print(find(arr))