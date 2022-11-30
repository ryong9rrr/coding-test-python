import math
def get_divisors(number):
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

def solution(number, limit, power):
    divisor_counts = []
    for num in range(1, number + 1):
        divisor_count = len(get_divisors(num))
        if divisor_count > limit:
            divisor_counts.append(power)
        else:
            divisor_counts.append(divisor_count)
    
    return sum(divisor_counts)
"""
정확성  테스트
테스트 1 〉	통과 (34.67ms, 10.4MB)
테스트 2 〉	통과 (5.71ms, 10.4MB)
테스트 3 〉	통과 (2.37ms, 10.3MB)
테스트 4 〉	통과 (7.36ms, 10.3MB)
테스트 5 〉	통과 (1.83ms, 10.2MB)
테스트 6 〉	통과 (34.72ms, 10.3MB)
테스트 7 〉	통과 (7.30ms, 10.3MB)
테스트 8 〉	통과 (4.27ms, 10.3MB)
테스트 9 〉	통과 (33.77ms, 10.4MB)
테스트 10 〉	통과 (2.56ms, 10.3MB)
테스트 11 〉	통과 (778.32ms, 10.8MB)
테스트 12 〉	통과 (821.70ms, 10.7MB)
테스트 13 〉	통과 (777.47ms, 10.7MB)
테스트 14 〉	통과 (1080.08ms, 10.8MB)
테스트 15 〉	통과 (850.78ms, 10.7MB)
테스트 16 〉	통과 (882.86ms, 10.8MB)
테스트 17 〉	통과 (0.01ms, 10.4MB)
테스트 18 〉	통과 (955.21ms, 10.7MB)
테스트 19 〉	통과 (10.38ms, 10.4MB)
테스트 20 〉	통과 (5.58ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.2MB)
테스트 24 〉	통과 (900.15ms, 10.7MB)
테스트 25 〉	통과 (907.10ms, 10.9MB)
테스트 26 〉	통과 (1.88ms, 10.2MB)
테스트 27 〉	통과 (1.54ms, 10.3MB)
"""