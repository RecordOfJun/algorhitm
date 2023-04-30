import sys
from collections import deque

def munji(arr,r,c):
    temp_arr=[[0]*c for _ in range(r)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(r):
        for j in range(c):
            if arr[i][j]==0:
                continue
            if arr[i][j]==-1:
                temp_arr[i][j]=-1
                continue
            cnt=0
            for k in range(4):
                x=i+dx[k]
                y=j+dy[k]
                if x==r or x==-1 or y==c or y==-1:
                    continue
                if arr[x][y]==-1:
                    continue
                cnt+=1
                temp_arr[x][y]+=arr[i][j]//5
            temp_arr[i][j]+=arr[i][j]-(arr[i][j]//5)*cnt
    return temp_arr

def filter(arr,r,c,device):
    up=device[0]
    down=device[1]
    upx=[-1,0,1,0]
    upy=[0,1,0,-1]
    downx=[1,0,-1,0]
    downy=[0,1,0,-1]
    x,y=up
    i=0
    x=x+upx[i]
    y=y+upy[i]
    arr[x][y]=0
    while True:
        if x+upx[i]==-1 or x+upx[i]==up[0]+1 or y+upy[i]==c:
            i+=1
            continue
        x = x + upx[i]
        y = y + upy[i]
        if x==up[0] and y==up[1]:
            break
        arr[x-upx[i]][y-upy[i]]=arr[x][y]
        arr[x][y]=0

    x,y=down
    i=0
    x=x+downx[i]
    y=y+downy[i]
    arr[x][y]=0
    while True:
        if x+downx[i]==r or x+downx[i]==down[0]-1 or y+downy[i]==c:
            i+=1
            continue
        x = x + downx[i]
        y = y + downy[i]
        if x==down[0] and y==down[1]:
            break
        arr[x-downx[i]][y-downy[i]]=arr[x][y]
        arr[x][y]=0



input=sys.stdin.readline
r,c,t=map(int,input().split(" "))
arr=[]
for _ in range(r):
    arr.append(list(map(int,input().split(" "))))

device=[]

for i in range(r):
    for j in range(c):
        if arr[i][j]==-1:
            device.append((i,j))

up_first=[]
up_second=[]
up_third=[]
up_fourth=[]

for i in range(t):
    arr=munji(arr,r,c)
    filter(arr,r,c,device)
cnt=0
for i in range(r):
    for j in range(c):
        if arr[i][j]==-1:
            continue
        cnt+=arr[i][j]

print(cnt)