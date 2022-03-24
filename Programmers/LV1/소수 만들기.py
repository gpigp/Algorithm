from itertools import combinations

def solution(nums):
    answer = 0

    n = list(combinations(nums, 3))
    for n_ in n:
        sum_ = sum(n_)
        num = 0
        for i in range(2,sum_):
            if sum_%i == 0:
                pass
            else:
                num += 1
        if num == sum_-2:
            answer += 1
    return answer