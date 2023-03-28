n,m=map(int,input().split(" "))
arr=[]
cnt_h=dict()
for _ in range(n):
    arr.append(input())
distance=0
dna=""
for i in range(m):
    cnt_h["A"]=0
    cnt_h["C"]=0
    cnt_h["G"]=0
    cnt_h["T"]=0
    for j in range(n):
        cnt_h[arr[j][i]]+=1
    cnt_h[cnt_h["T"]]="T"
    cnt_h[cnt_h["G"]]="G"
    cnt_h[cnt_h["C"]]="C"
    cnt_h[cnt_h["A"]]="A"
    result=max(cnt_h["A"],cnt_h["C"],cnt_h["G"],cnt_h["T"])
    dna+=cnt_h[result]
    distance+=n-result

print(dna)
print(distance)