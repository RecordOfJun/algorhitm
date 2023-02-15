n=int(input())
list=map(int,input().split())
list=sorted(list)
cnt=0
for i in range(n):
    for j in range(i+1):
        cnt+=list[j]
print(list)
print(cnt)