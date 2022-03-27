def solution(n):
    
    answer = 0
    for i in range(1, n+1):
        k = [i]
        while sum(k) <= n:            
            if sum(k) == n:
                answer += 1
                break
            k.append(k[-1]+1)
    
    return answer