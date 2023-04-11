import itertools
def isOk(i,j,x,y):
    d=abs(i-x)+abs(j-y)
    if d>2:
        return True
    return False

def price(arr,x,y):
    dx=[0,0,0,1,-1]
    dy=[0,1,-1,0,0]
    price_sum=0
    for i in range(5):
        price_sum+=arr[x+dx[i]][y+dy[i]]
    return price_sum

n=int(input())
arr=[]
idx=[]
for _ in range(n):
    arr.append(list(map(int,input().split(" "))))

for i in range(1,n-1):
    for j in range(1,n-1):
        idx.append((i,j))

cases=list(itertools.combinations(idx,3))
min_price=3000
for case in cases:
    a=case[0]
    b=case[1]
    c=case[2]
    if isOk(a[0],a[1],b[0],b[1]) and isOk(a[0],a[1],c[0],c[1]) and isOk(c[0],c[1],b[0],b[1]):
        p=price(arr,a[0],a[1])+price(arr,b[0],b[1])+price(arr,c[0],c[1])
        if p<min_price:
            min_price=p
        if min_price==0:
            print(0)
            exit()
print(min_price)