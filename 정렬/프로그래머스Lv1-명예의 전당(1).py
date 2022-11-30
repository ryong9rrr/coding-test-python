def solution(k, scores):
    result = []
    honors = []
    for score in scores:
        honors.append(score)
        honors.sort(reverse = True)
        honors = honors[:k]
        result.append(honors[-1])
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 9.99MB)
테스트 6 〉	통과 (0.01ms, 9.97MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.1MB)
테스트 12 〉	통과 (0.86ms, 10.1MB)
테스트 13 〉	통과 (1.04ms, 10.1MB)
테스트 14 〉	통과 (0.78ms, 10.2MB)
테스트 15 〉	통과 (1.86ms, 10.2MB)
테스트 16 〉	통과 (1.22ms, 10.2MB)
테스트 17 〉	통과 (1.31ms, 10.2MB)
테스트 18 〉	통과 (1.11ms, 10.2MB)
테스트 19 〉	통과 (0.52ms, 10.1MB)
테스트 20 〉	통과 (0.36ms, 10.1MB)
테스트 21 〉	통과 (0.36ms, 10.2MB)
테스트 22 〉	통과 (0.60ms, 10.2MB)
테스트 23 〉	통과 (0.59ms, 10.1MB)
테스트 24 〉	통과 (0.72ms, 10.3MB)
테스트 25 〉	통과 (0.73ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
"""