def solution(lottos, win_nums):
    answer = [0,0]
    lo_list = {x:0 for x in set(lottos)}
    
    for w in win_nums:
        for l in lo_list:
            if w == l:
                lo_list[w] += 1
    
    lo_num = 0
    for i in lo_list:
        lo_num += lo_list[i]
    
    zero_num = 0
    for i in range(len(lottos)):
        if lottos[i]==0:
            zero_num += 1
    
    answer[0] = 7-lo_num-zero_num
    answer[1] = 7-lo_num
    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6
       
    return answer