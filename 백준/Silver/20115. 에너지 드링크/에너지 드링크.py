n=int(input())
heap=list(map(int,input().split(" ")))
heap.sort()

total=0
for i in range(n-1):
    total+=heap[i]
    

print("%g"%(heap[n-1]+total/2))