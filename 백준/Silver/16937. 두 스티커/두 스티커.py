def find(w,h,w1,h1,w2,h2):
    a=(w1,h1)
    b=(w-w2,h-h2)
    if (w1<=w and h1<=h) and (w2<=w and h2<=h) and (a[0]<=b[0] or a[1]<=b[1]):
        return True
    return False

import itertools
h,w=map(int,input().split(" "))
n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split(" "))
    arr.append((a,b))

cases=list(itertools.combinations(arr,2))
maxwidth=0
for case in cases:
    w1,h1=case[0]
    w2,h2=case[1]
    #1.둘다 원래대로
    if find(w,h,w1,h1,w2,h2):
        maxwidth=max(maxwidth,w1*h1+w2*h2)
        continue
    #2.첫번째만 회전
    if find(w,h,h1,w1,w2,h2):
        maxwidth=max(maxwidth,w1*h1+w2*h2)
        continue
    #3.두번째만 회전
    if find(w,h,w1,h1,h2,w2):
        maxwidth=max(maxwidth,w1*h1+w2*h2)
        continue
    #4.둘 다 회전
    if find(w,h,h1,w1,h2,w2):
        maxwidth=max(maxwidth,w1*h1+w2*h2)
        continue
print(maxwidth)