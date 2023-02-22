a,b=map(int,input().split())
cnt=1
while(True):
    num=str(b)[-1]
    last=int(num[-1])
    if b==a:
        print(cnt)
        exit()
    elif b<a or last in [3,5,7,9]:
        print(-1)
        exit()
    else:
        if last in [2,4,6,8,0]:
            b=int(b/2)
        elif last==1:
            b=b//10
        cnt+=1