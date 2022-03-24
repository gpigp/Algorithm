def solution(arr1, arr2):
    # answer = [[0]*len(arr2[0])]*len(arr1)
    # print(answer)
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    # print(answer)
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):        
            for m in range(len(arr1[0])):               
                answer[i][k] += (arr1[i][m] * arr2[m][k])
    return answer