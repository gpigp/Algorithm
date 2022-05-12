import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
dict_ = defaultdict(list)

for _ in range(N-1):
    i, k = map(int, input().split())
    dict_[i].append(k)
    dict_[k].append(i)
    
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(dict_[k]) == 1:
            print("no")
            continue
    print("yes")