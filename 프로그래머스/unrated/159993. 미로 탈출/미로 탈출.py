from collections import deque
   
def solution(maps):
    start=()
    n=len(maps)
    m=len(maps[0])
    for i in range(n):
        for j in range(m):
            if(maps[i][j]=='S'):
                start=(i,j)
    
    
    visit_arr=[[False]*m for _ in range(n)]
    cnt_arr=[[0]*m for _ in range(n)]
    queue=deque()
    queue.append(start)
    cntL=0
    cntE=0
    findL=False
    findE=False
    idxL=()
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    visit_arr[start[0]][start[1]]=True
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(nx>=n or nx<0 or ny<0 or ny>=m):
                continue
            if(maps[nx][ny]=='X'):
                continue
            if(visit_arr[nx][ny]==False):
                visit_arr[nx][ny]=True
                cnt_arr[nx][ny]=cnt_arr[x][y]+1
                queue.append((nx,ny))
                if(maps[nx][ny]=='L'):
                    findL=True
                    cntL=cnt_arr[nx][ny]
                    idxL=(nx,ny)
                    break
                    
    if findL==False:
        return -1
        
    else:
        visit_arr=[[False]*m for _ in range(n)]
        cnt_arr=[[0]*m for _ in range(n)]
        queue=deque()
        queue.append((idxL[0],idxL[1]))
        visit_arr[idxL[0]][idxL[1]]=True
        while queue:
            x,y=queue.popleft()

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if(nx>=n or nx<0 or ny<0 or ny>=m):
                    continue
                if(maps[nx][ny]=='X'):
                    continue
                if(visit_arr[nx][ny]==False):
                    visit_arr[nx][ny]=True
                    cnt_arr[nx][ny]=cnt_arr[x][y]+1
                    queue.append((nx,ny))
                    if(maps[nx][ny]=='E'):
                        findE=True
                        cntE=cnt_arr[nx][ny]
                        break
        if(findE==False):
            return -1
    
    
    answer = cntE+cntL
    return answer

maps=["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))