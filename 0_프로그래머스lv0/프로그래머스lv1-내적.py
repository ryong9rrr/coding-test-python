def solution(a, b):
    result = 0
    for i in range(0, len(a)):
        result += a[i]*b[i]
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (0.16ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.4MB)
"""