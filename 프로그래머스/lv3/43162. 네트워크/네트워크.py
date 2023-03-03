from collections import deque
def solution(n, computers):
    answer = 0
    visited=[0]*n
    for i in range(n):
        if visited[i]!=0:
            continue
        answer+=1
        visited[i]=1
        queue=deque()
        queue.append(i)
        while queue:
            i=queue.popleft()
            for j in range(n):
                if(computers[i][j]==1 and visited[j]==0):
                    visited[j]=1
                    queue.append(j)
        
        
    return answer