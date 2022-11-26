def get_inclination(dotA, dotB):
    dx = dotB[0] - dotA[0]
    dy = dotB[1] - dotA[1]
    return dy / dx

def solution(dots):
    dots.sort(key = lambda x:x[0])
    a, b, c, d = dots
    
    d1 = get_inclination(a, b)
    d2 = get_inclination(c, d)
    
    if d1 == d2:
        return 1
    return 0
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
"""