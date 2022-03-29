n = int(input())
t = []
p = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    
# dp[i+1]때문에 배열 8개로 정의
dp = [0 for i in range(n+1)]

# 뒤에서부터 줄어듦
for i in range(n-1, -1, -1):
    # t_n 만큼 시간이 지난게 n보다 크면, n+1 -> n으로 수익 그대로 저장
    if i + t[i] > n:
        dp[i] = dp[i+1]
    # t[i]일 뒤에 얻을 수익(p[i]) + n번째 날 수익 을 n+1번째 수익과 비교    
    else:
        dp[i] = max(p[i] + dp[i+t[i]], dp[i+1])

answer = dp[0]
print(answer)