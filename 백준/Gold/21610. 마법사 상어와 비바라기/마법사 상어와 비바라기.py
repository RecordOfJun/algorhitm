import sys
from collections import deque

def water_copy(arr,n,clouds):
    dx=[1,1,-1,-1]
    dy=[1,-1,1,-1]
    for cloud in clouds:
        x,y=cloud
        cnt=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==-1 or ny==-1 or nx==n or ny==n:
                continue
            if arr[nx][ny]==0:
                continue
            cnt+=1
        arr[x][y]+=cnt

def make_clouds(arr,waters,n):
    temp_clouds=set()
    for i in range(n):
        for j in range(n):
            if arr[i][j]>=2 and (i,j) not in waters:
                arr[i][j]-=2
                temp_clouds.add((i,j))
    return temp_clouds

def magic(arr,n,clouds,move):
    dx=[0,0,-1,-1,-1,0,1,1,1]
    dy=[0,-1,-1,0,1,1,1,0,-1]
    d,s=move
    waters=set()
    for cloud in clouds:
        x,y=cloud
        x=(x+dx[d]*s)%n
        y = (y + dy[d] * s) % n
        arr[x][y]+=1#물복사버그 배열에 넣기
        waters.add((x,y))

    water_copy(arr,n,waters)

    return make_clouds(arr,waters,n)


input=sys.stdin.readline
n,m=map(int,input().split(" "))
arr=[]
move=[]
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))

for _ in range(m):
    move.append(list(map(int,input().split(" "))))
clouds=set()
clouds.add((n-1,0))
clouds.add((n-1,1))
clouds.add((n-2,0))
clouds.add((n-2,1))

for moving in move:
    clouds=magic(arr,n,clouds,moving)

cnt=0
for i in range(n):
    for j in range(n):
        cnt+=arr[i][j]

print(cnt)