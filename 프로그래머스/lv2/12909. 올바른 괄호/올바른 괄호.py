from collections import deque
def solution(s):
    answer = True
    arr=deque(s)
    cnt1=0
    cnt2=0
    
    while arr:
        value=arr.popleft()
        if value=="(":
            cnt1+=1
        elif value==")":
            cnt2+=1
        if cnt1<cnt2:
            return False
    if cnt1!=cnt2:
        return False
    return True