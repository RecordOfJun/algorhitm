n=int(input())
t=int(input())
a=int(input())
cnt0=0
cnt1=0
cnt=1
i=-1
if a==0:
    while True:
        i=(i+1)%n
        cnt0+=1
        if cnt0==t:
            print(i)
            exit()
        i=(i+1)%n
        i=(i+1)%n
        cnt0+=1
        if cnt0==t:
            print(i)
            exit()
        i=(i+1)%n
        for _ in range(cnt+1):
            i=(i+1)%n
            cnt0+=1
            if cnt0==t:
                print(i)
                exit()
        for _ in range(cnt+1):
            i=(i+1)%n
        cnt+=1

if a==1:
    while True:
        i=(i+1)%n
        i=(i+1)%n
        cnt1+=1
        if cnt1==t:
            print(i)
            exit()
        i=(i+1)%n
        i=(i+1)%n
        cnt1+=1
        if cnt1==t:
            print(i)
            exit()
        for _ in range(cnt+1):
            i=(i+1)%n
        for _ in range(cnt+1):
            i=(i+1)%n
            cnt1+=1
            if cnt1==t:
                print(i)
                exit()
        cnt+=1