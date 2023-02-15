import sys
command=sys.stdin.readline().rstrip().split(" ")
n=int(command[0])
m=int(command[1])
list=dict()
for i in range(n):
    poketmon=sys.stdin.readline().rstrip()
    list[str(i+1)]=poketmon
    list[poketmon]=str(i+1)

for i in range(m):
    ask=sys.stdin.readline().rstrip()
    print(list[ask])