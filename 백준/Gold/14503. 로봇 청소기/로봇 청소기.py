n,m=map(int,input().split(" "))
r,c,d=map(int,input().split(" "))
arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split(" "))))
nr=[-1,0,1,0]
nc=[0,1,0,-1]
cnt=0
while True:
    if arr[r][c]==0:
        arr[r][c]=2
        cnt+=1
    if arr[r-1][c]!=0 and arr[r][c-1]!=0 and arr[r+1][c]!=0 and arr[r][c+1]!=0:
        if arr[r-nr[d]][c-nc[d]]==1:
            break
        else:
            r=r-nr[d]
            c=c-nc[d]
            continue
    else:
        while True:
            d=(d-1)%4
            if arr[r+nr[d]][c+nc[d]]==0:
                r+=nr[d]
                c+=nc[d]
                break
print(cnt)