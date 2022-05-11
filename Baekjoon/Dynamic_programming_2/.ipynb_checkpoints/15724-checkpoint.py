import sys
input = lambda : sys.stdin.readline().rstrip()

size = list(map(int, input().split()))
N = size[0]
M = size[1]

rec = []
for _ in range(N):
    rec.append(list(map(int, input().split())))

K = int(input())
for _ in range(K):
    list_ = list(map(int, input().split()))
    sum_ = 0
    for i in range(list_[0]-1,list_[2]):
        sum_ += sum(rec[i][list_[1]-1 : list_[3]])
    print(sum_)
