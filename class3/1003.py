import time
cache=[0 for _ in range(41)]
cache[0]=[1,0];
cache[1]=[0,1];
cache[2]=[1,1];
def fibonacci(n,cache):
    if(n>2):
        for i in range(3,n+1):
            cache[i]=[cache[i-1][0]+cache[i-2][0],cache[i-1][1]+cache[i-2][1]]
    return cache[n];


n=int(input());
for i in range(n):
    num=int(input())
    cnt=fibonacci(num,cache)
    print("%d %d"%(cnt[0],cnt[1]));