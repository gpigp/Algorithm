n = int(input())

case = []

for i in range(n):
    case.append(int(input()))    
    
for i in case:
    fibo = [[1,0], [0,1]]
    if i > 1:
        for r in range(2,i+1):
            fibo.append([fibo[r-2][0]+fibo[r-1][0], 
                         fibo[r-2][1]+fibo[r-1][1]])
    print(fibo[i][0], fibo[i][1])