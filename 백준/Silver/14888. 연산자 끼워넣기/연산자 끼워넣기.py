import itertools
n=int(input())
num_arr=list(map(int,input().split(" ")))
a,b,c,d=map(int,input().split(" "))
arr=""
for _ in range(a):
    arr+="+"
for _ in range(b):
    arr+="-"
for _ in range(c):
    arr+="*"
for _ in range(d):
    arr+="/"
max_num=-10e+16
min_num=10e+16
cases=set(itertools.permutations(arr,len(arr)))
for case in cases:
    init=num_arr[0]
    i=1
    for item in case:
        if item=="+":
            init+=num_arr[i]
            i+=1
            continue
        if item=="-":
            init-=num_arr[i]
            i+=1
            continue
        if item=="*":
            init*=num_arr[i]
            i+=1
            continue
        if item=="/":
            if init<0:
                init=((init*-1)//num_arr[i])*-1
            else:
                init=init//num_arr[i]
            i+=1
            continue
    if init>max_num:
        max_num=init
    if init<min_num:
        min_num=init

print(max_num)
print(min_num)