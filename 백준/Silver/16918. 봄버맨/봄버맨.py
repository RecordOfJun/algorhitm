import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
from collections import deque

def displosion(x,y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx==r or nx==-1 or ny==c or ny==-1:
            continue
        if status[(nx,ny)]==0:
            continue
        boom.remove((nx,ny))
        status[(nx,ny)]=0
        arr[nx][ny] = '.'

def move():
    des=[]
    for item in boom:
        i,j=item
        status[(i,j)]+=1
        if status[(i, j)] == 3:
            des.append((i,j))
            arr[i][j] = '.'
            status[(i, j)] = 0
    for d in des:
        x, y = d
        boom.remove((x, y))
    for d in des:
        x,y=d
        displosion(x,y)

def install():
    for i in range(r):
        for j in range(c):
            if status[(i,j)]==0:
                boom.append((i,j))
                arr[i][j]='O'

def showResult():
    if cnt==n:
        for i in range(r):
            for j in range(c):
                print(arr[i][j],end="")
            print()
        exit()

def show(result):
    for i in range(r):
        for j in range(c):
            print(result[i][j], end="")
        print()

def copy():
    l=[[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            l[i][j]=arr[i][j]
    return l

r,c,n=map(int,input().split(" "))
arr=[]
boom=[]
result=[]
cnt=0
status=defaultdict(int)
for i in range(r):
    string=input()
    l=[]
    for j in range(c):
        l.append(string[j])
        if string[j]=='O':
            boom.append((i,j))
    arr.append(l)


move()
cnt+=1#봄버맨은 아무것도 하지 않는다
showResult()
move()
install()
cnt+=1#3 완료
showResult()
result.append(copy())
move()
cnt+=1
showResult()
result.append(copy())
move()
install()
cnt+=1#3 완료
showResult()
result.append(copy())
move()
cnt+=1
showResult()
result.append(copy())
# move()
# install()
# cnt+=1#3 완료
# showResult()
# result.append(copy())
# move()
# cnt+=1
# showResult()
# result.append(copy())


show(result[(n-2)%4])