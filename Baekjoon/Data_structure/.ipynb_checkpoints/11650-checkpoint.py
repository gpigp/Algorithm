import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

xy = sorted(xy, key = lambda x : (x[0], x[1]))
# xy.sort(key = lamdba x: (x[0], x[1]))
for i in xy:
    print(i[0], i[1])
