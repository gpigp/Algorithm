def solution(land):
             
    for i in range(1, len(land)):
        for k in range(4):
            land[i][k] += max(land[i-1][:k]+land[i-1][k+1:])

    return max(land[-1])

# 시간 초과
# land = land[1:] 효율 보다 for문 한번 돌리는게 더 빠름 
# while은 결국 for문의 연장선
def solution_2(land):
             
    while len(land) > 1:
        for k in range(4):
            land[1][k] = land[1][k] + max(land[0][:k]+land[0][k+1:])
                
        land = land[1:]
        
    answer = max(land[-1])
    
    return answer