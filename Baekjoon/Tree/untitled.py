import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

tree = []
while True:
    try :
        tree.append(int(input()))
    except :
        break

def post(start, end):
    if start > end:
        return
    else :
        root = tree[start]
        