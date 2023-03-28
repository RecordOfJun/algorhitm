import itertools
n=int(input())
m=int(input())
arr=[]

for _ in range(n):
    arr.append(input())

permutation=list(itertools.permutations(arr,m))
result=set()
for items in permutation:
    num=""
    for item in items:
        num+=item
    result.add(num)
print(len(result))