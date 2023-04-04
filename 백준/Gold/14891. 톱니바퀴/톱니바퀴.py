from collections import deque
def turnLeft(queue):
    queue.append(queue.popleft())

def turnRight(queue):
    queue.appendleft(queue.pop())


queue1=deque(input())
queue2=deque(input())
queue3=deque(input())
queue4=deque(input())

n=int(input())

for _ in range(n):
    num,d=map(int,input().split(" "))
    if num==1:#오른쪽 세개
        if d==-1:
            if queue1[2]!=queue2[6]:
                if queue2[2]!=queue3[6]:
                    if queue3[2]!=queue4[6]:
                        turnRight(queue4)
                    turnLeft(queue3)
                turnRight(queue2)
            turnLeft(queue1)
        else:
            if queue1[2]!=queue2[6]:
                if queue2[2]!=queue3[6]:
                    if queue3[2]!=queue4[6]:
                        turnLeft(queue4)
                    turnRight(queue3)
                turnLeft(queue2)
            turnRight(queue1)
    if num==2:#왼쪽 하나 오른쪽 두개
        if d==-1:
            if queue1[2]!=queue2[6]:
                turnRight(queue1)
            if queue2[2]!=queue3[6]:
                if queue3[2]!=queue4[6]:
                    turnLeft(queue4)
                turnRight(queue3)
            turnLeft(queue2)
        else:
            if queue1[2]!=queue2[6]:
                turnLeft(queue1)
            if queue2[2]!=queue3[6]:
                if queue3[2]!=queue4[6]:
                    turnRight(queue4)
                turnLeft(queue3)
            turnRight(queue2)
    if num==3:#왼쪽 두개 오른쪽 세개
        if d==-1:
            if queue2[2]!=queue3[6]:
                if queue1[2]!=queue2[6]:
                    turnLeft(queue1)
                turnRight(queue2)
            if queue3[2]!=queue4[6]:
                turnRight(queue4)
            turnLeft(queue3)
        else:
            if queue2[2]!=queue3[6]:
                if queue1[2]!=queue2[6]:
                    turnRight(queue1)
                turnLeft(queue2)
            if queue3[2]!=queue4[6]:
                turnLeft(queue4)
            turnRight(queue3)
    if num==4:#왼쪽 세개
        if d==-1:
            if queue3[2]!=queue4[6]:
                if queue2[2]!=queue3[6]:
                    if queue1[2]!=queue2[6]:
                        turnRight(queue1)
                    turnLeft(queue2)
                turnRight(queue3)
            turnLeft(queue4)
        else:
            if queue3[2]!=queue4[6]:
                if queue2[2]!=queue3[6]:
                    if queue1[2]!=queue2[6]:
                        turnLeft(queue1)
                    turnRight(queue2)
                turnLeft(queue3)
            turnRight(queue4)
print(int(queue1[0])+int(queue2[0])*2+int(queue3[0])*4+int(queue4[0])*8)