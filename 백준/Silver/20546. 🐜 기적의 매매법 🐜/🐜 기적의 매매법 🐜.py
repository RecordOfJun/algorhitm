money=int(input())
last=-1
up=-1
down=0
bnpMoney=money
bnpStock=0
timingMoney=money
timingStock=0

price=list(map(int,input().split(" ")))
for i in range(14):
    stock=price[i]
    #bnp
    bnpCnt=bnpMoney//stock
    if(bnpCnt>0):
        bnpStock+=bnpCnt
        bnpMoney=bnpMoney%stock
    #timing
    if(stock>last):
        up+=1
        down=0
        if(up>=3 and timingStock>0):
            timingMoney+=timingStock*stock
            timingStock=0
    elif(stock<last):
        down+=1
        up=0
        if(down>=3 and timingMoney//stock>0):
            timingStock+=timingMoney//stock
            timingMoney=timingMoney%stock
    last=stock
    if(i==13):
        bnp=bnpMoney+bnpStock*stock
        timing=timingMoney+timingStock*stock
        if(bnp>timing):
            print("BNP")
        elif(bnp<timing):
            print("TIMING")
        else:
            print("SAMESAME")