from itertools import *
def solution(users, emoticons):
    answer = []
    n=len(emoticons)
    all_case=list(product([10,20,30,40],repeat=n))
    result=[]
    for case in all_case:
        sub=0
        price=0
        for user in users:
            buy=0
            for i in range(n):
                if(case[i]>=user[0]):
                    buy+=int(emoticons[i]*(100-case[i])/100)
            if(buy>=user[1]):
                sub+=1
            else:
                price+=buy
        result.append((sub,price))
    
    arr=sorted(result,key= lambda x : (-x[0],-x[1]))
    answer.append(arr[0][0])
    answer.append(arr[0][1])
    return answer