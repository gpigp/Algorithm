import sys
input = lambda : sys.stdin.readline().rstrip()
N=int(input())
A=list(map(int, input().split()))

dp = [0 for _ in range(N)]
for i in range(N):
    for k in range(i):
        if A[i] > A[k] and dp[i] < dp[k]:
            dp[i] = dp[k]
    dp[i] += 1
print(max(dp))