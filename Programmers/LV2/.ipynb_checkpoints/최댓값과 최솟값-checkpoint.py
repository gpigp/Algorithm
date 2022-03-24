def solution(s):
    
    a = [int(i) for i in s.split()]
    
    return " ".join([str(min(a)),str(max(a))])