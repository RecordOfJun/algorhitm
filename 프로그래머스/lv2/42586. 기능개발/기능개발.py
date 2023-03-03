from collections import deque
def solution(progresses, speeds):
    answer = []
    pro_q=deque(progresses)
    sp_q=deque(speeds)
    
    while pro_q:
        cnt=0
        while pro_q[0]<100:
            for i,value in enumerate(pro_q):
                pro_q[i]+=sp_q[i]
        while pro_q and pro_q[0]>=100:
            pro_q.popleft()
            sp_q.popleft()
            cnt+=1
        answer.append(cnt)
        
    return answer