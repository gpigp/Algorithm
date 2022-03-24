def solution(n):
    
    a = [0, 1, 1]

    for i in range(n-2):
        a.append(a[-1]+a[-2])
    
    return (a[-1])%1234567