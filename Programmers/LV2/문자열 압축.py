def solution(s):

    min_len = len(s)

    for i in range(1,len(s)//2+1):
        s_ = s
        a = ""
        a_ = ""
        num = 1
        while len(s_) > 0:
            if s_[0:i] == s_[i:2*i]:
                num += 1
                a = s_[0:i]
                if len(s_) == 2*len(s_[i:]):
                    a_ += str(num)
                    a_ += a
                    break
                s_ = s_[i:]
            else:
                if num > 1:
                    a_ += str(num)
                    a_ += a

                else:
                    a_ += s_[0:i]
                s_ = s_[i:]
                num = 1
        if min_len > len(a_):
            min_len = len(a_)

    answer = min_len
    return answer