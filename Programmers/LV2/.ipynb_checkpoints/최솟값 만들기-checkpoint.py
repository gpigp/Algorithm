def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    
    C = 0
    for i in range(len(A)):
        C += (A[i]*B[-1-i])

    return C