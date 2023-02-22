import sys
n=int(input())
dis=list(map(int,input().split(" ")))
price=list(map(int,input().split(" ")))

total=0
minimum=price[0]
for i in range(n-1):
    if(minimum>price[i]):
        minimum=price[i]
    total+=minimum*dis[i]

print(total)