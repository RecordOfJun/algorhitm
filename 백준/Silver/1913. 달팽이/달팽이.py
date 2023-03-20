n=int(input())
arr=[[" "]*n for _ in range(n)]
m=int(input())
x=0
y=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
idx=[]
i=0
num=n*n
while num>0:
    arr[x][y]=num
    nx=x+dx[i]
    ny=y+dy[i]
    if num==m:
        idx.append(x)
        idx.append(y)
    if nx<0 or ny<0 or nx>=n or ny>=n or arr[nx][ny]!=" ":
        i=(i+1)%4
        nx=x+dx[i]
        ny=y+dy[i]
    x=nx
    y=ny
    num-=1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

print("%d %d"%(idx[0]+1,idx[1]+1))