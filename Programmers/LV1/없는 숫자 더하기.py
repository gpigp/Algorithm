def solution(numbers):

    n = [i for i in range(10)]

    for i in numbers:
        n.remove(i)

    return sum(n)