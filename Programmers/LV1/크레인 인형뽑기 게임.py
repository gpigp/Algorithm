def solution(board, moves):

    h = []
    answer = 0
    for m in moves:
        for b in range(len(board)):
            if board[b][m-1] > 0:
                h.append(board[b][m-1])
                # 뽑았으니 0으로 init
                board[b][m-1] = 0

                # 무조건 넣으니 2개이상일 때 비교
                if len(h) > 1:
                    now = h[-1]
                    before = h[-2]
                    if before == now:
                        answer += 2
                        h = h[:-2]
                break

    return answer