n=int(input())
fac=1;
for i in range(1,n+1):
    fac*=i;

divide=10
cnt=0
while(True):
    if(fac%divide!=0):
        break
    cnt+=1
    divide*=10

print(cnt)