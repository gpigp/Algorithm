n = int(input())

# dp에는 계산한 횟수를 저장
dp = [0 for i in range(1000001)]

for i in range(2, n+1):
    # 무조건 1을 뺀 상황이 생김 and 1을 뺀 횟수
    dp[i] = dp[i-1] + 1
    
    if i%2 ==0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 ==0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])

    
    