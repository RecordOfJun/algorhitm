import itertools
def convert(arr,i,j,di,dj):
    for k in range(3):
        if arr[i+di*k][j+dj*k]=="H":
            arr[i+di*k][j+dj*k]="T"
        else:
            arr[i+di*k][j+dj*k]="H"

def checkArr(arr):
    check=arr[0][0]
    for i in range(3):
        for j in range(3):
            if arr[i][j]!=check:
                return False
    return True


n=int(input())
cases=list(itertools.permutations(range(8),8))
for _ in range(n):
    arr=[]
    min_num=9
    for i in range(3):
        arr.append(list(input().split(" ")))
    if checkArr(arr):
        print(0)
        continue
    for case in cases:
        cnt=0
        newArr=[[""]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                newArr[i][j]=arr[i][j]
        for num in case:
            cnt+=1
            if num==0:
                convert(newArr,0,0,0,1)
            elif num==1:
                convert(newArr,1,0,0,1)
            elif num==2:
                convert(newArr,2,0,0,1)
            elif num==3:
                convert(newArr,0,0,1,0)
            elif num==4:
                convert(newArr,0,1,1,0)
            elif num==5:
                convert(newArr,0,2,1,0)
            elif num==6:
                convert(newArr,0,0,1,1)
            elif num==7:
                convert(newArr,2,0,-1,1)
            if checkArr(newArr):
                min_num=min(cnt,min_num)
                break
    if min_num==9:
        print(-1)
    else:
        print(min_num)