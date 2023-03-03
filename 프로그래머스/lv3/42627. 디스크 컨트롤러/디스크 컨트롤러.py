import heapq
from collections import deque
def solution(jobs):
    answer = 0
    heap=[]
    disk_heap=[]
    for job in jobs:
        heapq.heappush(heap,(job[0],job[1]))
    
    disk_sum=0
    whole=0
    
    while heap:
        while heap:
            i,length=heapq.heappop(heap)
            if(i<=disk_sum):
                heapq.heappush(disk_heap,(length,i))
            else:
                heapq.heappush(heap,(i,length))
                break
                
        if disk_heap:
            length,i=heapq.heappop(disk_heap)
            disk_sum+=length
            whole+=(disk_sum-i)
        else:
            disk_sum+=1
    
    while disk_heap:
        length,i=heapq.heappop(disk_heap)
        disk_sum+=length
        whole+=(disk_sum-i)
            
    return whole//len(jobs)