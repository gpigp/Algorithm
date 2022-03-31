import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
if n > 3:
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    dp[2] = max(s[0]+s[2], s[1]+s[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+s[i]+s[i-1], dp[i-2]+s[i])
else:
    if n == 3:
        dp[0] = s[0]
        dp[1] = s[0]+s[1]
        dp[2] = max(s[0]+s[2], s[1]+s[2])
    elif n == 2:
        dp[0] = s[0]
        dp[1] = s[0]+s[1]
    elif n == 1:
        dp[0] = s[0]

print(dp[-1])