n=int(input())
if(n==1 or n==3):
    print("-1")
    exit();
else:
    max=n//5
    cnt5=max
    while(True):
        sub=n-cnt5*5
        if(sub%2==0):
            total=cnt5+sub//2
            print(total)
            exit();
        cnt5=cnt5-1