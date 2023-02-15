import sys
command=sys.stdin.readline().rstrip().split(" ")
n=int(command[0])
m=int(command[1])
list1=dict()
list2=[]
for i in range(n):
    name=sys.stdin.readline().rstrip()
    list1[name]=True

cnt=0
for i in range(m):
    name=sys.stdin.readline().rstrip()
    try:
        if(list1[name]):
            cnt+=1
            list2.append(name)
    except:
        pass

print(cnt)
list2=sorted(list2)
for i in range(len(list2)):
    print(list2[i])