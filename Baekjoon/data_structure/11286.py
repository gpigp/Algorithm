import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
small=[]

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(small, (abs(x),x))
    else:
        if small:
            print(heapq.heappop(small)[1])
        else:
            print(0)
