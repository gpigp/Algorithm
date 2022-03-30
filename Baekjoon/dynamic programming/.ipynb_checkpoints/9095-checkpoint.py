t = int(input())
n = []
for i in range(t):
    n.append(int(input()))

def dp(k):
    dp_ = [0,1,2,4]
    if k >= 4:
        for i in range(4,k+1):
            dp_.append(dp_[i-1]+dp_[i-2]+dp_[i-3])
    return dp_[k]
for i in n:
    
    answer = dp(i)
    
    print(answer)