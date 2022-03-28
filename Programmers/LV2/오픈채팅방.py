from collections import defaultdict

def solution(record):
    
    userid = defaultdict()
    
    answer = []
    
    for i in record:
        if i.split()[0] == "Enter":
            userid[i.split()[1]] = i.split()[2]
        elif i.split()[0] == "Change":
            userid[i.split()[1]] = i.split()[2]
    for i in record:
        if i.split()[0] == "Enter":
            answer.append(userid[i.split()[1]] + "님이 들어왔습니다.")
        elif i.split()[0] == "Leave":
            answer.append(userid[i.split()[1]] + "님이 나갔습니다.")
    
    return answer