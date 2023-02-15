n=int(input())
temp=[n]
cnt=0
while(1 not in temp):
    falseList=[]
    for i in temp:
        if(i%3==0):
            falseList.append(i/3)
        if(i%2==0):    
            falseList.append(i/2)
        if(i-1>=1):    
            falseList.append(i-1)
    cnt+=1
    temp=list(set(falseList))

print(cnt,temp)