# 이게 왜 레벨 2...?
def solution(s):
    numbers = sorted(map(int, s.split()))
    return f"{numbers[0]} {numbers[-1]}"
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
"""