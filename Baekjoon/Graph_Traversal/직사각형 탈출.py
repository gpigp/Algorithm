import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
square = deque()
N, M = map(int, input().split())

for _ in range(M):
    square.append(map(int, input().split()))
print(square[0])