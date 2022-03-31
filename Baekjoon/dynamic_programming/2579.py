import sys
input = sys.stdin.readline
n = int(input())
score = [0]
for i in range(n): 
    score.append(int(input()))

answer = score[-1]
for i in range(n-3, -1, -1):
    answer += score[i]+ max(score[i+1], score[i+2])

print(answer)