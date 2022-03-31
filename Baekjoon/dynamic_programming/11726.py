import sys
input = sys.stdin.readline()

n = int(input)

def tile(n):
    t = [0,1,2]
    if n > 2:
        for i in range(3,n+1):
            t.append(t[i-2] + t[i-1])
    return t[n]
answer = tile(n)%10007
print(answer)