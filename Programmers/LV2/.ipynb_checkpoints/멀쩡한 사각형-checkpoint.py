import math

def solution(w,h):
    
    return w*h - (w+h-math.gcd(w,h))

# 시간초과, w and h가 짝수인 경우로 나누어 해봐도 테스트11에서 시간초과
def solution2(w,h):
    
    y = 0
    a = -h/w
    for i in range(1, w):
        y += int(a*i + h)
    return y*2    