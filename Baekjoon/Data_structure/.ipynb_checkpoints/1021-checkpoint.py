import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
pos = list(map(int, input().split()))
dq = deque([i for i in range(1,N+1)])

cnt = 0
for i in pos:
    while True:
        if i==dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1
print(cnt)