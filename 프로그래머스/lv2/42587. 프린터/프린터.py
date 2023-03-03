from collections import deque
import heapq
def solution(priorities, location):
    answer = 0
    queue=deque((value,i) for i,value in enumerate(priorities))
    sorted_queue=deque(sorted(priorities,reverse=True))
    
    cnt=0
    while queue:
        value,i=queue.popleft()
        if value!=sorted_queue[0]:
            queue.append((value,i))
        else:
            sorted_queue.popleft()
            cnt+=1
            if(i==location):
                return cnt
    return answer