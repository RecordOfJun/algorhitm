import copy
from collections import defaultdict
def Rotate(arr,idx,d,RB):
    di=[0,0,0,-1,1]#왼,오,위,아래
    dj=[0,-1,1,0,0]
    i=idx[0]+di[d]
    j=idx[1]+dj[d]
    while arr[i][j]=='.':
        i+=di[d]
        j+=dj[d]
    if arr[i][j]=='O':
        arr[idx[0]][idx[1]]='.'
        idx=[-1,-1]
    else:
        arr[idx[0]][idx[1]]='.'
        arr[i-di[d]][j-dj[d]]=RB
        idx=[i-di[d],j-dj[d]]
    return idx

def check(idxR,idxB):
    if idxB==[-1,-1]:
        return 1
    elif idxR==[-1,-1]:
        return 2
    else:
        return 0

def left(arr,idxR,idxB):
    if idxR[1]<idxB[1]:
        idxR=Rotate(arr,idxR,1,'R')
        idxB=Rotate(arr,idxB,1,'B')
    else:
        idxB=Rotate(arr,idxB,1,'B')
        idxR=Rotate(arr,idxR,1,'R')
    
    return arr,idxR,idxB
    
        

def right(arr,idxR,idxB):
    if idxR[1]>idxB[1]:
        idxR=Rotate(arr,idxR,2,'R')
        idxB=Rotate(arr,idxB,2,'B')
    else:
        idxB=Rotate(arr,idxB,2,'B')
        idxR=Rotate(arr,idxR,2,'R')

    return arr,idxR,idxB

def up(arr,idxR,idxB):
    if idxR[0]<idxB[0]:
        idxR=Rotate(arr,idxR,3,'R')
        idxB=Rotate(arr,idxB,3,'B')
    else:
        idxB=Rotate(arr,idxB,3,'B')
        idxR=Rotate(arr,idxR,3,'R')

    return arr,idxR,idxB

def down(arr,idxR,idxB):
    if idxR[0]>idxB[0]:
        idxR=Rotate(arr,idxR,4,'R')
        idxB=Rotate(arr,idxB,4,'B')
    else:
        idxB=Rotate(arr,idxB,4,'B')
        idxR=Rotate(arr,idxR,4,'R')

    return arr,idxR,idxB

def dfs(cnt,arr,idxR,idxB,min_cnt,cases):
    a=""
    a+=str(idxR[0])
    a+=str(idxR[1])
    a+=str(idxB[0])
    a+=str(idxB[1])
    if cases[a]!=0 and cases[a]<=cnt:
        return 11
    cases[a]=cnt
    if cnt>=min_cnt[0]:
        return 11
    
    c=check(idxR,idxB)

    if c==2:
        min_cnt[0]=cnt
        return cnt
    if c==1:
        return 11
    else:
        l=left(copy.deepcopy(arr),copy.deepcopy(idxR),copy.deepcopy(idxB))
        r=right(copy.deepcopy(arr),copy.deepcopy(idxR),copy.deepcopy(idxB))
        u=up(copy.deepcopy(arr),copy.deepcopy(idxR),copy.deepcopy(idxB))
        d=down(copy.deepcopy(arr),copy.deepcopy(idxR),copy.deepcopy(idxB))
        return min(dfs(cnt+1,l[0],l[1],l[2],min_cnt,cases),dfs(cnt+1,r[0],r[1],r[2],min_cnt,cases),dfs(cnt+1,u[0],u[1],u[2],min_cnt,cases),dfs(cnt+1,d[0],d[1],d[2],min_cnt,cases))


n,m=map(int,input().split(" "))
arr=[[0]*m for _ in range(n)]
idxR=[0,0]
idxB=[0,0]
cases=defaultdict(int)
min_cnt=[]
min_cnt.append(11)
for i in range(n):
    string=input()
    for j in range(m):
        arr[i][j]=string[j]
        if arr[i][j]=="R":
            idxR=[i,j]
            continue
        if arr[i][j]=="B":
            idxB=[i,j]
            continue
result=dfs(0,arr,idxR,idxB,min_cnt,cases)

if result==11:
    print(-1)
else:
    print(result)