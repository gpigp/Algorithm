import math

def dec(p):
    if p >= 2:
        for i in range(2, int(math.sqrt(p))+1):
            if p%i == 0:
                return False
    else:
        return False
    return True

def solution(n, k):
    
    num = []
    while n > 0:
        num.append(str(n%k))
        n = n//k
    num.reverse()
    
    zero = []
    for i, nu in enumerate(num):
        if nu == "0":
            zero.append(i)
            
    p = ""
    answer = 0
    # P
    if len(zero) == 0:
        p = "".join(num)
        if dec(int(p)) == True:
            answer += 1
    else:
        # P0
        if zero[0] >= 1:
            p = "".join(num[:zero[0]])
            if dec(int(p)) == True:
                answer += 1
        # 0P
        if zero[-1] < len(num)-1:
            p = "".join(num[zero[-1]+1:])
            if dec(int(p)) == True:
                answer += 1
        # 0P0
        if len(zero) >= 2:
            for i, z in enumerate(zero[:-1]):
                p = "".join(num[z+1:zero[i+1]])
                if p != "" and dec(int(p)) == True:
                    answer += 1
            
    return answer

# 다른 사람 풀이
def sol2(n, k):
    num = ""
    answer = 0
    
    while n > 0:
        num += str(n%k)
        n = n//k
    num = num[::-1]
    
    for i in num.split("0"):
        if i == "":           ## if not i: 로 대체 가능
            pass
        elif dec(int(i)):
            answer += 1
    
    return answer