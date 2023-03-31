import itertools
from collections import defaultdict
t=input()
char_num=defaultdict(int)

for text in t:
    char_num[text]+=1

n=int(input())
arr=[]
for _ in range(n):
    price,title=input().split(" ")
    arr.append((int(price),title))

cases=[]
min_pirce=100000*16+1
for i in range(1,n+1):
    com=list(itertools.combinations(arr,i))
    for item in com:
        cases.append(item)

for case in cases:
    price_sum=0
    text_sum=""
    for item in case:
        price=item[0]
        title=item[1]
        price_sum+=price
        text_sum+=title
    if min_pirce<price_sum:
        continue
    temp_num=defaultdict(int)
    for text in text_sum:
        temp_num[text]+=1
    isOk=True
    for key in char_num.keys():
        if(char_num[key]>temp_num[key]):
            isOk=False
            break
    if isOk:
        min_pirce=price_sum
if min_pirce==100000*16+1:
    print(-1)
else:
    print(min_pirce)