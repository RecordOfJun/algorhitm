sentence=input().split("-")
result=0
for i in range(len(sentence)):
    sum=0
    arr=sentence[i].split("+")
    for j in range(len(arr)):
        sum+=int(arr[j])
    if(i==0):
        result+=sum
    else:
        result-=sum

print(result)