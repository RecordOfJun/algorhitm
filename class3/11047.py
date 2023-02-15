command=input().split(" ")
n=int(command[0])
k=int(command[1])

list=[]
for i in range(n):
    list.append(int(input()))
cnt=0
for i in range(n-1,-1,-1):
    if(k>=list[i]):
        cnt+=k//list[i]
        k=k%list[i]
    if(k==0):
        break

print(cnt)
