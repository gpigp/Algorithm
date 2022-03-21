def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    # key, value인 dictionary 타입 사용
    repo_list = {x:0 for x in id_list}
    
    # set 타입으로 중복 제거
    for r in set(report):
        # 각 사람당 신고당한 횟수 찾기
        repo_list[r.split()[1]] += 1
        
    for r in set(report):
        # k 이상 신고당했을 경우
        if repo_list[r.split()[1]] >= k:
            # 신고한 몇명의 유저가 정지 당한지 기록
            answer[id_list.index(r.split()[0])] += 1
        
                
    return answer