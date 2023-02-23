n,m=map(int,input().split(" "))
s_list=list(map(int,input().split(" ")))
d_list=list(map(int,input().split(" ")))
p_list=[0 for _ in range(n)]

for _ in range(m):
    for i in range(n):
        p_list[d_list[i]-1]=s_list[i]

    for i in range(n):
        s_list[i]=p_list[i]

for i in range(n):
    print(p_list[i],end=" ")