from collections import defaultdict
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    n=len(completion)
    for i in range(n):
        if(participant[i]!=completion[i]):
            return participant[i]
    return participant[n]