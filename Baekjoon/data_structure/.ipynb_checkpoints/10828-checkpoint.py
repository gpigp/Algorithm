import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
stk = []
for _ in range(N):
    i = input()
    
    # push X: 정수 X를 스택에 넣는 연산이다.
    if i.split()[0] == "push":
        stk.append(int(i.split()[1]))
        
    # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
    elif i == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
            stk = stk[:-1]
            
    # size: 스택에 들어있는 정수의 개수를 출력한다.        
    elif i == "size":
        print(len(stk))
        
    # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.    
    elif i == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)
            
    # top: 스택의 가장 위에 있는 정수를 출력한다.
    elif i == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])