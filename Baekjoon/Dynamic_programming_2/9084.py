import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    unit = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1
    for i in unit:
        for k in range(M+1):
            if k >= i:
                dp[k] += dp[k-i]
    print(dp[M])
    