import sys
n,m=map(int,input().split())
list={}
for i in range(n):
    command=sys.stdin.readline().rstrip().split(" ");
    list[command[0]]=command[1]

for i in range(m):
    command=sys.stdin.readline().rstrip()
    print(list[command])