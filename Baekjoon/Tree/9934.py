import sys
input = lambda : sys.stdin.readline().rstrip()
K = int(input())
dog = list(map(int, input().split()))
Tree = [[] for _ in range(K)]

def BT(dog, i):
    mid = len(dog)//2
    Tree[i].append(str(dog[mid]))
    if len(dog) != 1:
        BT(dog[:mid], i+1)
        BT(dog[mid+1:], i+1)
    
BT(dog, 0)
for i in range(K):
    answer = " ".join(Tree[i])
    print(answer)