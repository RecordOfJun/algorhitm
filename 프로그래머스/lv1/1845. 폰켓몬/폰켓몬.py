def solution(nums):
    answer = 0
    n=len(nums)
    cnt=len(list(set(nums)))
    if(n//2<cnt):
        answer=n//2
    else:
        answer=cnt
    return answer