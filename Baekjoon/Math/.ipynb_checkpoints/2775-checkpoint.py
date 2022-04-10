import sys
input = lambda : sys.stdin.readline().rstrip()
T = int(input())
test = [[] for _ in range(T)]

for i in range(T):
    test[i].append(int(input()))
    test[i].append(int(input()))
    
def live(k, n):
    floor = [j+1 for j in range(n)]
    for i in range(1, k+1):
        n_floor = [1]
        for r in range(1, n):
            n_floor.append(floor[r] + n_floor[-1])
        floor = n_floor    
    print(floor[-1])

for i in range(T):
    live(test[i][0], test[i][1])