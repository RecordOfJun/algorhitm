n=int(input())
classes=list(map(int,input().split(" ")))
b,c=map(int,input().split(" "))
cnt=n

for student in classes:
    sub=student-b
    if sub>0:
        if sub%c>0:
            cnt+=sub//c+1
        else:
            cnt+=sub//c

print(cnt)