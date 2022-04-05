from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
que = deque()
for _ in range(N):
    i = input()
    
    if i.split()[0] == "push":
        que.append(i.split()[1])
        
    elif i == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.popleft()
            
    elif i == "size":
        print(len(que))
        
    elif i == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
            
    elif i == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            
    elif i == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])