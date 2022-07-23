def solution(left, right):
    #제곱수를 가지면 무조건 약수의 개수는 홀수임
    result = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            result -= i
        else:
            result += i
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.44ms, 10.3MB)
테스트 2 〉	통과 (0.21ms, 10.3MB)
테스트 3 〉	통과 (0.17ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.30ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
"""

# 2022년 7월
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

def solution(left, right):
    result = 0
    for number in range(left, right + 1):
        n = len(get_divisor(number))
        if n % 2 == 0:
            result += number
        else:
            result -= number
    return result
"""
정확성  테스트
테스트 1 〉	통과 (1.84ms, 10.3MB)
테스트 2 〉	통과 (0.50ms, 10.2MB)
테스트 3 〉	통과 (0.86ms, 10.2MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (1.51ms, 10.1MB)
테스트 6 〉	통과 (0.14ms, 10.2MB)
테스트 7 〉	통과 (0.16ms, 10.2MB)
"""