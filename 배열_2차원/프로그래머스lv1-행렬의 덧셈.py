import numpy as np
def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    answer = a+b
    return answer.tolist()

"""
정확성  테스트
테스트 1 〉	통과 (1.01ms, 27.6MB)
테스트 2 〉	통과 (0.78ms, 27.5MB)
테스트 3 〉	통과 (0.33ms, 27.9MB)
테스트 4 〉	통과 (1.19ms, 27.6MB)
테스트 5 〉	통과 (1.37ms, 27.5MB)
테스트 6 〉	통과 (0.18ms, 27.5MB)
테스트 7 〉	통과 (1.13ms, 27.6MB)
테스트 8 〉	통과 (0.13ms, 27.7MB)
테스트 9 〉	통과 (1.17ms, 28.2MB)
테스트 10 〉	통과 (0.91ms, 27.7MB)
테스트 11 〉	통과 (0.55ms, 28.2MB)
테스트 12 〉	통과 (0.76ms, 28.3MB)
테스트 13 〉	통과 (0.55ms, 28.2MB)
테스트 14 〉	통과 (0.72ms, 28MB)
테스트 15 〉	통과 (2.23ms, 28MB)
테스트 16 〉	통과 (3.29ms, 28MB)
테스트 17 〉	통과 (32.75ms, 41MB)
"""

# 2중 반복문
def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    
    result = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(arr1[i][j] + arr2[i][j])
        result.append(temp)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.27ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.11ms, 10.3MB)
테스트 6 〉	통과 (0.22ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.15ms, 10.3MB)
테스트 9 〉	통과 (0.96ms, 10.9MB)
테스트 10 〉	통과 (0.76ms, 10.8MB)
테스트 11 〉	통과 (0.57ms, 10.5MB)
테스트 12 〉	통과 (0.58ms, 10.7MB)
테스트 13 〉	통과 (0.47ms, 10.6MB)
테스트 14 〉	통과 (0.57ms, 10.6MB)
테스트 15 〉	통과 (0.63ms, 10.7MB)
테스트 16 〉	통과 (0.63ms, 10.6MB)
테스트 17 〉	통과 (30.26ms, 22.9MB)
"""

# 2중 zip()
def solution(arr1, arr2):
    result = []
    for x, y in list(zip(arr1, arr2)):
        temp = []
        for w, z in list(zip(x, y)):
            temp.append(w + z)
        result.append(temp)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.22ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.11ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (0.92ms, 10.9MB)
테스트 10 〉	통과 (0.58ms, 10.8MB)
테스트 11 〉	통과 (0.37ms, 10.5MB)
테스트 12 〉	통과 (0.66ms, 10.7MB)
테스트 13 〉	통과 (0.35ms, 10.7MB)
테스트 14 〉	통과 (0.47ms, 10.6MB)
테스트 15 〉	통과 (0.59ms, 10.7MB)
테스트 16 〉	통과 (0.49ms, 10.6MB)
테스트 17 〉	통과 (21.75ms, 22.9MB)
"""