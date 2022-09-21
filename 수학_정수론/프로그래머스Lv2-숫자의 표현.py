# 브루트포스
def solution(n):
    count = 0
    
    for start_number in range(1, n + 1):
        total = 0
        while total < n:
            total += start_number
            start_number += 1
        if total == n:
            count += 1
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.20ms, 10.1MB)
테스트 3 〉	통과 (0.15ms, 10.2MB)
테스트 4 〉	통과 (0.15ms, 10.1MB)
테스트 5 〉	통과 (0.05ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (0.12ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.48ms, 10MB)
테스트 11 〉	통과 (0.46ms, 10.1MB)
테스트 12 〉	통과 (0.17ms, 10.1MB)
테스트 13 〉	통과 (0.31ms, 9.99MB)
테스트 14 〉	통과 (0.17ms, 10MB)
테스트 15 〉	통과 (0.00ms, 9.98MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.02ms, 10.1MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (3.80ms, 10.2MB)
테스트 2 〉	통과 (2.50ms, 10.3MB)
테스트 3 〉	통과 (3.08ms, 10.2MB)
테스트 4 〉	통과 (3.05ms, 10.2MB)
테스트 5 〉	통과 (3.30ms, 9.99MB)
테스트 6 〉	통과 (3.44ms, 10.2MB)
"""

# 정수론) 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수는 주어진 수의 홀수 약수의 개수와 같다.
import math
def get_divisor(number):
    if number <= 0:
        raise Exception("자연수가 아니에요.")
    limit = math.floor(math.sqrt(number))
    divisors = []
    for left in range(1, limit + 1):
        if number % left == 0:
            right = number // left
            divisors.append(left)
            if left != right:
                divisors.append(right)
    return divisors

def solution(n):
    divisors = get_divisor(n)
    return len([x for x in divisors if x % 2 == 1])
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10MB)
효율성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
"""

# 모든 약수를 구하지 않더라도
def solution(n):
    count = 0
    # n 이하의 모든 홀수들이
    for x in range(1, n + 1, 2):
        # 나누어 떨어진다면
        if n % x == 0:
            count += 1
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 9.98MB)
효율성  테스트
테스트 1 〉	통과 (0.41ms, 10.2MB)
테스트 2 〉	통과 (0.28ms, 10.2MB)
테스트 3 〉	통과 (0.32ms, 10.2MB)
테스트 4 〉	통과 (0.30ms, 10.3MB)
테스트 5 〉	통과 (0.37ms, 10.1MB)
테스트 6 〉	통과 (0.19ms, 10.2MB)
"""