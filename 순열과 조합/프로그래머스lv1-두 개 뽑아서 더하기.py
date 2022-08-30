def solution(numbers):
    SIZE = len(numbers)
    result = set([])
    for i in range(SIZE - 1):
        for j in range(i + 1, SIZE):
            total = numbers[i] + numbers[j]
            result.add(total)
    
    # python에서는 집합자료형도 배열처럼 사용가능
    return sorted(result)
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.42ms, 10.2MB)
테스트 8 〉	통과 (0.43ms, 10.3MB)
테스트 9 〉	통과 (0.41ms, 10.2MB)
"""

# itertools 조합 메서드 사용
from itertools import combinations
def solution(numbers):
    result = set([])
    for a, b in list(combinations(numbers, 2)):
        result.add(a + b)
    return sorted(result)
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.78ms, 10.2MB)
테스트 8 〉	통과 (0.71ms, 10.2MB)
테스트 9 〉	통과 (0.87ms, 10.2MB)
"""