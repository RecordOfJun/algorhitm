import sys
from collections import deque

def magic(arr,n):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    evenodd=[0,2,4,6]
    mix=[1,3,5,7]
    temp_arr=[[[]for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not arr[x][y]:
                continue
            for ball in arr[x][y]:
                m,s,d=ball
                nx=(x+dx[d]*s)%n
                ny=(y+dy[d]*s)%n
                temp_arr[nx][ny].append([m,s,d])

    for x in range(n):
        for y in range(n):
            if not temp_arr[x][y]:
                continue
            cnt=len(temp_arr[x][y])
            if cnt==1:
                continue
            m_sum=0
            s_sum=0
            even_cnt=0
            odd_cnt=0
            while temp_arr[x][y]:
                m,s,d=temp_arr[x][y].pop()
                m_sum+=m
                s_sum+=s
                if d%2==0:
                    even_cnt+=1
                else:
                    odd_cnt+=1
            if m_sum//5==0:
                continue

            for i in range(4):
                if even_cnt==0 or odd_cnt==0:
                    temp_arr[x][y].append([m_sum//5,s_sum//cnt,evenodd[i]])
                else:
                    temp_arr[x][y].append([m_sum//5,s_sum//cnt,mix[i]])
    return temp_arr
input=sys.stdin.readline
n,m,k=map(int,input().split(" "))
arr=[[[]for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,m,s,d=map(int,input().split(" "))
    arr[r-1][c-1].append([m,s,d])


for _ in range(k):
    arr=magic(arr,n)

result=0
for i in range(n):
    for j in range(n):
        for ball in arr[i][j]:
            result+=ball[0]

print(result)