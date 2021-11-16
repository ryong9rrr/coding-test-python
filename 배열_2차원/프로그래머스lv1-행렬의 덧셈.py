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