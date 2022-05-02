import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

# 비어있거나, 방향이 존재
tree = defaultdict()
k = 1
while True:
    line = list(map(int, input().split()))
    if len(line) > 0 and line[-1] == -1:
        break
        
    for node in line:
        if node != 0:
            tree[node]=0
    for i, node in enumerate(line):
        if i%2 != 0 and node !=0:
            tree[node] += 1
            
    if len(line) > 0 and line[-1] == 0:
        print("Case", k, end=" ")
        len_ = 0
        flag = True
        
        for i in tree:
            if tree[i] == 0:
                len_ += 1
            elif tree[i] > 1:
                flag = False
        if len_ != 1 :
            flag = False
            
        if flag or len(tree) == 0:
            print("is a tree.")
        else:
            print("is not a tree.")
        k += 1
        tree = defaultdict()
        continue