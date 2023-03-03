from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    arrived=[]
    bridge=deque([0]*(bridge_length-1))
    trucks=deque(truck_weights)
    n=len(truck_weights)
    arrived_cnt=0
    time_cnt=1
    bridge_sum=0
    while arrived_cnt<n:
        time_cnt+=1
        if trucks and bridge_sum+trucks[0]<=weight:
            value=trucks.popleft()
            bridge.append(value)
            bridge_sum+=value
        else:
            bridge.append(0)
        
        value=bridge.popleft()
        if value!=0:
            arrived.append(value)
            bridge_sum-=value
            arrived_cnt+=1
    
    answer=time_cnt
    return answer