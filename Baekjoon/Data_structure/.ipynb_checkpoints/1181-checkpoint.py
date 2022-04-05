import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
word=[]
for _ in range(N):
    word.append(input())
    
word = sorted(set(word), key=lambda x: (len(x), x))
for i in word:
    print(i)