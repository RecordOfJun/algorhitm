from collections import defaultdict,deque
def findwords(target,words,n,friends):
    for word in words:
        cnt=0
        for i in range(n):
            if(word[i]!=target[i]):
                cnt+=1
        if cnt==1:
            friends[target].append(word)
            friends[word].append(target)
            
def solution(begin, target, words):
    answer = 0
    n=len(words)
    m=len(words[0])
    friends=defaultdict(list)
    check=defaultdict(int)
    findwords(begin,words,m,friends)
    for i in range(n-1):
        findwords(words[i],words[i+1:],m,friends)
        
    queue=deque()
    queue.append(begin)
    while queue:
        value=queue.popleft()
        for friend in friends[value]:
            if friend==target:
                return check[value]+1
            if check[friend]!=0:
                continue
            check[friend]=check[value]+1
            queue.append(friend)
    return 0