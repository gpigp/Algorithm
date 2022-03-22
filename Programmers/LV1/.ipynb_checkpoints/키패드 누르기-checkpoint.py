def solution(numbers, hand):
    
    answer = ''
    num = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    lh = [(n,m) for n in range(4) for m in range(3) if num[n][m]=="*"]
    rh = [(n,m) for n in range(4) for m in range(3) if num[n][m]=="#"]

    for i in numbers:
        if i in [1,4,7]:
            lh = [(n,m) for n in range(4) for m in range(3) if num[n][m]==i]
            answer += "L"
        elif i in [3,6,9]:
            rh = [(n,m) for n in range(4) for m in range(3) if num[n][m]==i]
            answer += "R"
        elif i in [2,5,8,0]:
            mh = [(n,m) for n in range(4) for m in range(3) if num[n][m]==i]
            ll = abs(lh[0][0]-mh[0][0])+abs(lh[0][1]-mh[0][1])
            rl = abs(rh[0][0]-mh[0][0])+abs(rh[0][1]-mh[0][1])
            if ll > rl:
                rh = mh
                answer += "R"
            elif ll < rl:
                lh = mh
                answer += "L"
            elif ll == rl:
                if hand == "right":
                    rh = mh
                    answer += "R"
                else:
                    lh = mh
                    answer += "L"
                    
    return answer