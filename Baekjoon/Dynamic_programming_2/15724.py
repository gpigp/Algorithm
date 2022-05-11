import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

rec = []
for _ in range(int(N)):
    rec.append(list(map(int, input().split())))

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for k in range(1,M+1):
        dp[i][k] = rec[i-1][k-1] + dp[i-1][k] + dp[i][k-1] - dp[i-1][k-1]
        # 위 식이 중요

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    susi = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(susi)
