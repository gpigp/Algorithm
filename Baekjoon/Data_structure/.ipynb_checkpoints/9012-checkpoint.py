import sys
input = lambda : sys.stdin.readline().rstrip()
# from collections import Counters

n = int(input())

for _ in range(n):
    a = input()
    flag = True
    b = []
    for i in a:
        if not b:
            if i == ")":
                print("NO")
                flag = False
                break
            b.append(i)
        else:
            if i == "(":
                b.append(i)
            else:
                b.pop()
    if flag and not b:
        print("YES")
    elif b:
        print("NO")