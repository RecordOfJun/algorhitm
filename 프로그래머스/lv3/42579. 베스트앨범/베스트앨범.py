from collections import defaultdict
import heapq
def solution(genres, plays):
    answer = []
    genre_dict=defaultdict(list)
    play_sum=defaultdict(int)
    n=len(plays)
    
    for i in range(n):
        genre=genres[i]
        play=plays[i]
        #장르별로 플레이 수랑 해당 인덱스 넣기
        heapq.heappush(genre_dict[genre],(-play,i))
        #장르별 플레이 수 저장
        play_sum[genre]+=play
        
    arr=[]
    
    for key in list(play_sum.keys()):
        heapq.heappush(arr,(-play_sum[key],key))
    
    
    while arr:
        temp,key=heapq.heappop(arr)
        
        cnt=0
        while genre_dict[key]:
            answer.append(heapq.heappop(genre_dict[key])[1])
            cnt+=1
            if(cnt==2):
                break
    
    return answer