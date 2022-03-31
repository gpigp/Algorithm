import sys
input = lambda : sys.stdin.readline().rstrip()
# from collections import Counters

# n = int(input())
a = '(()())((()))'

b = []
# for i in a:
#     if i=='(':
#         b.append(i)
#     elif i==')' and len(b)>0:
#         if b.pop() == '(':
#             pass
#     else:
#         print("NO")
#         break
# 0 [] {}

flag = True
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

if flag:
    print("YES")