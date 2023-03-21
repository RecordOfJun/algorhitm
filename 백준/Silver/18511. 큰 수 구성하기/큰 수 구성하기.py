from collections import deque
n,k=map(int,input().split(" "))
nums=list(map(int,input().split(" ")))
nums.sort()
cnt=1
arr=deque()
for item in nums:
    arr.append(item)
while arr:
    pop=arr.popleft()
    for item in nums:
        result=pop*10+item
        if result>n:
            if arr:
                print(arr.pop())
            else:
                print(pop)
            exit()
        arr.append(result)