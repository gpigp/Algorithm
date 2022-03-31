import sys
input = sys.stdin.readline

N = int(input())
dp = []
for i in range(N):
    dp.append(list(map(int, input().strip().split())))  

for r in range(1,N):
    for i in range(3):
        dp[r][i] += min(dp[r-1][:i]+dp[r-1][i+1:])

# for r in range(1,N):
#     dp[r][0] = dp[r][0] + min(dp[r-1][1], dp[r-1][2])
#     dp[r][1] = dp[r][1] + min(dp[r-1][0], dp[r-1][2])
#     dp[r][2] = dp[r][2] + min(dp[r-1][1], dp[r-1][0])
        
print(min(dp[-1]))