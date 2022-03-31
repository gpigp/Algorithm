import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
list_ =[]
for _ in range(N):
    list_.append(int(input()))

for i in sorted(list_):
    print(i)
