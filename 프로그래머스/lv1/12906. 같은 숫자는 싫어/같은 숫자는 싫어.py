from collections import deque
def solution(arr):
    answer = []
    queue=deque(arr)
    
    last=""
    while queue:
        value=queue.popleft()
        if value!=last:
            answer.append(value)
            last=value
    return answer