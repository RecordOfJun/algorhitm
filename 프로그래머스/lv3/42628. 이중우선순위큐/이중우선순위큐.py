from bisect import bisect_left,bisect_right
from collections import deque
def solution(operations):
    answer = []
    oper_q=deque(operations)
    num_q=deque()
    while oper_q:
        oper=oper_q.popleft()
        oper1,oper2=oper.split(" ")
        
        if oper1=="I":
            num_q.insert(bisect_left(num_q,int(oper2)),int(oper2))
            continue
        if oper=="D 1":
            if num_q:
                num_q.pop()
            continue
        if oper=="D -1":
            if num_q:
                num_q.popleft()
            continue
    if num_q:
        return [num_q.pop(),num_q.popleft()]
    else:
        return [0,0]