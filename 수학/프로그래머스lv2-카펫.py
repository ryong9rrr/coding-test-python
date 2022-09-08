def solution(brown, yellow):
    _sum = brown + yellow
    
    for i in range(3, int(_sum ** 0.5) + 1):
        if _sum / i == int(_sum / i):
            x = i
            y = int(_sum / i)
            if (x - 2) * (y - 2) == yellow:
                return [y, x]
        
    return print("입력 값이 올바르지 않아요.")

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.26ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.14ms, 10.3MB)
테스트 8 〉	통과 (0.18ms, 10.3MB)
테스트 9 〉	통과 (0.16ms, 10.3MB)
테스트 10 〉	통과 (0.20ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
"""

# 22년 9월 풀이
def solution(brown, yellow):
    total = brown + yellow
    
    for x in range(2, int(total ** 0.5) + 1):
        b = total / x
        if b != int(b):
            continue
        y = int(b)
        if (x - 2) * (y - 2) == yellow:
            return sorted([x, y], reverse = True)
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.16ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.1MB)
테스트 8 〉	통과 (0.17ms, 10.3MB)
테스트 9 〉	통과 (0.14ms, 10.3MB)
테스트 10 〉	통과 (0.37ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
"""