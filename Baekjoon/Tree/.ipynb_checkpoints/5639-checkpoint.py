import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

num = []
while True:
    try:
        num.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    else:
        root = num[start]
        div = end + 1
        for pos in range(start+1, end+1):
            if root < num[pos]:
                div = pos
                break
        post(start+1, div-1)
        post(div, end)
        print(root)
        
post(0, len(num)-1)