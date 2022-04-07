import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
Parent = list(map(int, input().split()))
remove = int(input())
Tree = {}

for i in range(N):
    Tree[i] = [Parent[i], 0]
for i in range(N):
    if Parent[i] != -1:
        Tree[Parent[i]][1] += 1
    
def DFS(graph, num):
    graph[num][1] = -2
    # 부모가 -1인 경우는 부모 노드가 없다는 뜻이므로 자식노드 개수 안 없애줘도 됨.
    if graph[num][0] != -1:
        graph[graph[num][0]][1] -= 1
    for i in range(N):
        if graph[i][0] == num:
            DFS(graph, i)
DFS(Tree, remove)

leaf_cnt = 0
for i in range(N):
    if Tree[i][1] == 0:
        leaf_cnt += 1

print(leaf_cnt)
