import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

L = int(input())
word = input()
letter = defaultdict()

for i in word:
    letter[i] = 0
for i in word:
    letter[i] += 1

# letter = sorted(letter, reverse=True)
if max(letter.values()) == 1:
    print(0)
else:
    print(max(letter.values()))