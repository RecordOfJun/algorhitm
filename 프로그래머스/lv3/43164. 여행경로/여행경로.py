from collections import defaultdict,deque
import itertools
import heapq
    
def solution(tickets):
    answer = []
    m=len(tickets)+1
    ticket_dict=defaultdict(list)
    for ticket in tickets:
        heapq.heappush(ticket_dict[ticket[0]],ticket[1])
    
    whole_case=[]
    order=[]
    for key in list(ticket_dict.keys()):
        arr=[]
        while ticket_dict[key]:
            arr.append(heapq.heappop(ticket_dict[key]))
        whole_case.append(list(itertools.permutations(arr)))
        order.append(key)
    
    arr=list(itertools.product(*whole_case))
    n=len(order)
    for items in arr:
        new_dict=defaultdict(deque)
        for i in range(n):
            new_dict[order[i]]=deque(items[i])
        queue=deque()
        answer=[]
        queue.append("ICN")
        while queue:
            value=queue.popleft()
            answer.append(value)
            if new_dict[value]:
                queue.append(new_dict[value].popleft())
        if len(answer)==m:
            break
    return answer