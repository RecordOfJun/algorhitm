from collections import deque
def check_cross_left(bingo):
    if(bingo[1,1]==-1 and bingo[2,2]==-1 and bingo[3,3]==-1 and bingo[4,4]==-1 and bingo[5,5]==-1):
        return True
    return False

def check_cross_right(bingo):
    if(bingo[1,5]==-1 and bingo[2,4]==-1 and bingo[3,3]==-1 and bingo[4,2]==-1 and bingo[5,1]==-1):
        return True
    return False

def check_width(i,bingo):
    if(bingo[i,1]==-1 and bingo[i,2]==-1 and bingo[i,3]==-1 and bingo[i,4]==-1 and bingo[i,5]==-1):
        return True
    return False

def check_height(j,bingo):
    if(bingo[1,j]==-1 and bingo[2,j]==-1 and bingo[3,j]==-1 and bingo[4,j]==-1 and bingo[5,j]==-1):
        return True
    return False

bingo=dict()
idx=dict()
j=1
queue=deque()
for i in range(1,6):
    arr=list(map(int,input().split(" ")))
    j=1
    for item in arr:
        bingo[i,j]=item
        idx[item]=(i,j)
        j+=1

cnt=0
bingo_cnt=0
for i in range(5):
    queue.append(list(map(int,input().split(" "))))

while queue:
    arr=queue.popleft()
    for item in arr:
        i,j=idx[item]
        bingo[i,j]=-1
        cnt+=1
        if check_width(i,bingo):
            bingo_cnt+=1
        if check_height(j,bingo):
            bingo_cnt+=1
        if i==j and check_cross_left(bingo):
            bingo_cnt+=1
        if i+j==6 and check_cross_right(bingo):
            bingo_cnt+=1
        if(bingo_cnt>=3):
            print(cnt)
            exit()
