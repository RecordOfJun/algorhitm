from collections import deque
import copy
def destroy(arr,d,s,n):
    dx=[0,-1,1,0,0]
    dy=[0,0,0,-1,1]
    for i in range(1,s+1):
        arr[n//2+dx[d]*i][n//2+dy[d]*i]=0

def convertToQueue(arr,n):
    queue=deque()
    check_arr=[[0]*n for _ in range(n)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x=0
    y=0
    i=0
    for _ in range(n*n-1):
        value=arr[x][y]
        if value!=0:
            queue.appendleft(value)
        check_arr[x][y]=1
        if x+dx[i]<0 or x+dx[i]>=n or y+dy[i]<0 or y+dy[i]>=n or check_arr[x+dx[i]][y+dy[i]]==1:
            i=(i+1)%4
        x=x+dx[i]
        y=y+dy[i]
    return queue

def converToArr(queue,n):
    arr=[[-1]*n for _ in range(n)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x=0
    y=0
    i=0
    while queue:
        value=queue.pop()
        arr[x][y]=value
        if x+dx[i]<0 or x+dx[i]>=n or y+dy[i]<0 or y+dy[i]>=n or arr[x+dx[i]][y+dy[i]]!=-1:
            i=(i+1)%4
        x=x+dx[i]
        y=y+dy[i]
    arr[n//2][n//2]=0
    return arr

def candyCrucsh(queue):
    new_queue=deque()
    cnt=0
    current=queue[0]
    flag=False
    destroyed=[0,0,0]
    while queue:
        value=queue.popleft()
        if value==current:
            cnt+=1
        else:
            if cnt<4:
                for _ in range(cnt):
                    new_queue.append(current)
            else:
                flag=True
                destroyed[current-1]+=cnt
            cnt=1
            current=value
    if cnt<4:
        for _ in range(cnt):
            new_queue.append(current)
    else:
        flag=True
        destroyed[current-1]+=cnt

    return (new_queue,flag,destroyed)

def multiply(queue,n):
    new_queue=deque()
    cnt=0
    current=queue[0]
    num=0
    while queue and num<n*n-1:
        value=queue.popleft()
        if value==current:
            cnt+=1
        else:
            new_queue.append(cnt)
            new_queue.append(current)
            num+=2
            cnt=1
            current=value
    if num<n*n-1:
        new_queue.append(cnt)
        new_queue.append(current)
        num+=2
    while num<n*n-1:
        new_queue.append(0)
        num+=1

    return new_queue

n,m=map(int,input().split(" "))
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))
destroyed=[0,0,0]
for _ in range(m):
    d,s=map(int,input().split(" "))
    destroy(arr,d,s,n)
    queue=convertToQueue(arr,n)
    if len(queue)==0:
        break
    isCrushed=True
    while isCrushed:
        result=candyCrucsh(queue)
        queue=result[0]
        for i in range(3):
            destroyed[i]+=result[2][i]
        isCrushed=result[1]
        if len(queue)==0:
            break
    if len(queue)==0:
        break
    queue=multiply(queue,n)
    arr=converToArr(queue,n)
    
print(destroyed[0]+destroyed[1]*2+destroyed[2]*3)