import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
list_ =[]
for _ in range(N):
    list_.append(int(input()))

for i in sorted(list_):
    print(i)
    
    
data = [[1,2], [1,3], [2, 3], [2, 5], [4, 3]]

data = sorted(data, key=lambda x : len(x))