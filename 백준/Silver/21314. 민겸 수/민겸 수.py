import math
n=input()
maxNum=""
minNum=""
cnt=0
for i in range(len(n)):
    #max
    if(n[i]=='K'):
        if(cnt!=0):
            minNum+="1"
            for j in range(cnt-1):
                minNum+="0"
            minNum+="5"

            maxNum+="5"
            for j in range(cnt):
                maxNum+="0"
        else:
            minNum+="5"
            maxNum+="5"
        cnt=0
    elif(i+1==len(n)):
        minNum+="1"
        maxNum+="1"
        for j in range(cnt):
            minNum+="0"
            maxNum+="1"
    else:
        cnt+=1
print(maxNum)
print(minNum)