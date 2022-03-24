def solution(s):
    
    s = list(s.lower())

    for i, alpha_ in enumerate(s):
        if s[0].isalpha():
            s[0] = s[0].upper()
        if i != 0 and s[i-1] == " " and s[i].isalpha():
            s[i] = s[i].upper()

    answer = "".join(s)
    
    return answer