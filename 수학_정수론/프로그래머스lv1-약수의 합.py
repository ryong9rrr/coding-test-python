import math
def get_divisor(number):
    if number < 0:
        raise Exception("숫자는 0 이상의 정수여아합니다.")
    if number == 0:
        return [0]
    divisors = []
    limit = math.floor(math.sqrt(number))
    for left in range(1, limit + 1):
        if number % left == 0:
            right = number // left
            if left == right:
                divisors.append(left)
            else:
                divisors.append(left)
                divisors.append(right)
    return divisors

def solution(n):
    return sum(get_divisor(n))
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
"""