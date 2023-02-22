board=input()
list=list(board)

cnt=0
for i in range(len(list)):
    if(list[i]=='X'):
        cnt+=1
        if(cnt==4):
            for j in range(4):
                list[i-j]='A'
            cnt=0
        elif(cnt==2 and i==len(list)-1):
            for j in range(2):
                list[i-j]='B'
            cnt=0
        elif(cnt==2 and list[i+1]!='X'):
            for j in range(2):
                list[i-j]='B'
            cnt=0
        elif(i==len(list)-1 and cnt%2==1):
            print(-1)
            exit()
    elif(cnt%2==1):
        print(-1)
        exit()

result="".join(list)
print(result)