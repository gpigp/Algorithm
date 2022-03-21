# First Try
'''
n = input()
list_ = list()
for i in range(int(n)):
    list_.append(int(input()))
    list_.sort()
    mid = int(i/2)
    if i%2==1:
        if list_[mid] > list_[mid+1]:
            print(list_[mid+1])
        else:
            print(list_[mid])
    else:
        print(list_[mid])
'''

# Second Try

import heapq
import sys

n = int(sys.stdin.readline())
lh = []
rh = []
for i in range(n):
    num = int(sys.stdin.readline())
    
    # 일단 좌우 힙에 넣기
    if len(lh) == len(rh):
        heapq.heappush(lh, -num)
    else:
        heapq.heappush(rh, num)
        
    # 위치 변경    
    if rh and -1*lh[0] > rh[0]:
        lh_v = heapq.heappop(lh)
        rh_v = heapq.heappop(rh)
        
        heapq.heappush(lh, -rh_v)
        heapq.heappush(rh, -lh_v)
    print(-lh[0])
    
    