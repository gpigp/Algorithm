import sys
sys.setrecursionlimit(10**9)

input = lambda : sys.stdin.readline().rstrip()
N = int(input())

Tree = [[] for _ in range(N+1)]

Parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

# <--------------------- DFS -------------------->

def DFS(s):
    for i in Tree[s]:
        if Parents[i] == 0:
            Parents[i] = s
            DFS(i)
            
DFS(1)
for i in range(2, N+1):
    print(Parents[i])
    
# <---------------------------------------------->

# # <--------------------- BFS -------------------->

# from collections import deque

# que = deque()
# que.append(1)

# def BFS():
#     while que:
#         s = que.popleft()
#         for i in Tree[s]:
#             if Parents[i] == 0:
#                 Parents[i] = s
#                 que.append(i)
# BFS()
# for i in range(2, N+1):
#     print(Parents[i])

# # <---------------------------------------------->
