import sys
from collections import defaultdict
import heapq
def isK(arr,r,c,k,row,col):
    if row<r or col<c:
        return False
    if arr[r-1][c-1]==k:
        return True
    return False

def spanCol(arr,row,col):
    max_col=col
    for i in range(row):
        count_dict=defaultdict(int)
        for j in range(col):
            num=arr[i][j]
            if num!=0:
                count_dict[arr[i][j]]+=1
        heap=[]
        keys=count_dict.keys()
        length=len(keys)*2
        if length>max_col:
            max_col=length
        for key in keys:
            heapq.heappush(heap,(count_dict[key],key))
        j=0
        while heap:
            if j==100:
                return
            value,key=heapq.heappop(heap)
            arr[i][j]=key
            arr[i][j+1]=value
            j+=2
        current_j=j
        for j in range(current_j,col):
            arr[i][j]=0
    col=max_col
    return col


def spanRow(arr,row,col):
    max_row=row
    for j in range(col):
        count_dict=defaultdict(int)
        for i in range(row):
            num = arr[i][j]
            if num != 0:
                count_dict[arr[i][j]] += 1
        heap = []
        keys = count_dict.keys()
        length = len(keys) * 2
        if length > max_row:
            max_row = length
        for key in keys:
            heapq.heappush(heap, (count_dict[key], key))
        i = 0
        while heap:
            if i==100:
                break
            value, key = heapq.heappop(heap)
            arr[i][j] = key
            arr[i+1][j] = value
            i += 2
        current_i = i
        for i in range(current_i, row):
            arr[i][j] = 0
    row = max_row
    return row

input=sys.stdin.readline

arr=[[0 for _ in range(100)]for _ in range(100)]
r,c,k=map(int,input().split(" "))

row=3
col=3

for i in range(3):
    q,w,e=map(int,input().split(" "))
    arr[i][0]=q
    arr[i][1]=w
    arr[i][2]=e
cnt=0
while not isK(arr,r,c,k,row,col):
    if cnt==100:
        print(-1)
        exit()
    cnt+=1
    if row>=col:
        col=spanCol(arr,row,col)
    else:
        row=spanRow(arr,row,col)

print(cnt)