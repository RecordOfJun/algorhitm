from collections import deque
def solution(numbers, target):
    answer=0
    n=len(numbers)
    queue=deque()
    queue.append([[numbers[0]],1])
    queue.append([[-numbers[0]],1])
    while queue:
        arr,length=queue.popleft()
        if(length==n):
            if sum(arr)==target:
                answer+=1
            continue
        left=arr[:]
        right=arr[:]
        left.append(numbers[length])
        right.append(-numbers[length])
        queue.append([left,length+1])
        queue.append([right,length+1])
    return answer