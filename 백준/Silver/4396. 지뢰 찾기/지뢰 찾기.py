#지뢰 입력 받으면 위치가 어디인지 저장
#지뢰 주면 9칸에 대해서 +1 해주기
#누른 칸에 대해서 지뢰가 아니면 그냥 값이 무엇인지 모여주기
#누른 칸이 지뢰이면 지뢰 위치 저장한 배열을 모두 돌아서 다 x표시해주기
def num_plus(x,y,arr_num):
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if(nx<0 or ny<0 or nx==n or ny==n):
            continue
        if(arr_num[nx][ny]=='*'):
            continue
        arr_num[nx][ny]+=1

n=int(input())
arr_num=[[0]*n for _ in range(n)]
arr_idx=[]

for i in range(n):
    line=input()
    j=0
    for item in line:
        if item=="*":
            arr_idx.append((i,j))
            arr_num[i][j]='*'
            num_plus(i,j,arr_num)
        j+=1

arr_result=[['.']*n for _ in range(n)]
flag=True
for i in range(n):
    line=input()
    j=0
    for item in line:
        if item=="x":
            if(arr_num[i][j]=='*'):
                if flag:
                    for item in arr_idx:
                        x,y=item
                        arr_result[x][y]='*'
                    flag=False
            else:
                arr_result[i][j]=arr_num[i][j]
        j+=1

for i in range(n):
    for j in range(n):
        print(arr_result[i][j],end="")
    print()