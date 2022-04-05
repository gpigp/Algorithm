import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())

# 받을 수 있는 범위를 수용할 배열 생성 후 처리
num = [0] * 10000
for _ in range(N):
    i = int(input())
    num[i-1] += 1

# 범위 안에서 그 숫자만큼 출력
for i in range(10000):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i+1)
        
# # 기본적인 정렬
# num = [int(input()) for _ in range(N)]
# num.sort()
# for i in num:
#     print(i)

# # 힙을 사용한 정렬
# import heapq
# num = []
# for _ in range(N):
#     number = int(input())
#     heapq.heappush(num, number)
# for _ in range(N):
#     print(heapq.heappop(num))
