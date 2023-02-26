from collections import deque
n=int(input())
queue=deque(input())
arr=[]
arr.append(queue.popleft())
last=arr[0]

while queue:
    value=queue.popleft()
    if(value!=last):
        last=value
        arr.append(last)

arr_length=len(arr)
print((arr_length+2)//2)