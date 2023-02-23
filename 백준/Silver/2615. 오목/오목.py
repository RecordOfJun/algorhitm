arr=[[0]*19 for _ in range(19)]
for i in range(19):
    row=list(map(int,input().split(" ")))
    for j in range(19):
        arr[i][j]=[row[j],False,False,False,False]

def first(num,arr,i,j):
    cnt=0
    while(i<19 and j<19 and arr[i][j][0]==num and cnt<=5):
        arr[i][j][1]=True#확인함
        cnt+=1
        i-=1
        j+=1
    if(cnt==5):
        return True
    else:
        return False
    
def second(num,arr,i,j):
    cnt=0
    while(i<19 and j<19 and arr[i][j][0]==num and cnt<=5):
        arr[i][j][2]=True#확인함
        cnt+=1
        j+=1
    if(cnt==5):
        return True
    else:
        return False

def third(num,arr,i,j):
    cnt=0
    while(i<19 and j<19 and arr[i][j][0]==num and cnt<=5):
        arr[i][j][3]=True#확인함
        cnt+=1
        i+=1
        j+=1
    if(cnt==5):
        return True
    else:
        return False

def fourth(num,arr,i,j):
    cnt=0
    while(i<19 and j<19 and arr[i][j][0]==num and cnt<=5):
        arr[i][j][4]=True#확인함
        cnt+=1
        i+=1
    if(cnt==5):
        return True
    else:
        return False

        

for j in range(19):
    for i in range(19):
        if(arr[i][j][0]==1 or arr[i][j][0]==2):
            if(arr[i][j][1]==False):
                result=first(arr[i][j][0],arr,i,j)
                if(result==True):
                    print(arr[i][j][0])
                    print("%d %d"%(i+1,j+1))
                    exit()
            if(arr[i][j][2]==False):
                result=second(arr[i][j][0],arr,i,j)
                if(result==True):
                    print(arr[i][j][0])
                    print("%d %d"%(i+1,j+1))
                    exit()
            if(arr[i][j][3]==False):
                result=third(arr[i][j][0],arr,i,j)
                if(result==True):
                    print(arr[i][j][0])
                    print("%d %d"%(i+1,j+1))
                    exit()
            if(arr[i][j][4]==False):
                result=fourth(arr[i][j][0],arr,i,j)
                if(result==True):
                    print(arr[i][j][0])
                    print("%d %d"%(i+1,j+1))
                    exit()

print(0)