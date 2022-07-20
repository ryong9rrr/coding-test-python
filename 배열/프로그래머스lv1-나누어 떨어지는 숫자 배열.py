def solution(arr, divisor):
    result = sorted([x for x in arr if x % divisor == 0])
    return result if result else [-1]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (3.26ms, 13.3MB)
테스트 7 〉	통과 (0.15ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.16ms, 10.1MB)
테스트 10 〉	통과 (0.07ms, 10.1MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.22ms, 10.1MB)
테스트 14 〉	통과 (0.09ms, 10.3MB)
테스트 15 〉	통과 (0.15ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.1MB)
"""