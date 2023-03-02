from collections import defaultdict
def solution(clothes):
    answer = 0
    default_dict=defaultdict(int)
    
    for cloth in clothes:
        default_dict[cloth[1]]+=1
    
    cnt=1
    
    for key in list(default_dict.keys()):
        cnt=cnt*(default_dict[key]+1)
        
    answer=cnt-1
    return answer