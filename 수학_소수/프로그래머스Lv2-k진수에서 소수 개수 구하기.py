# 일반적 에라토스테네스의 체 -> 문자열이 너무 커질 수 있기 때문에 오버플로우가 발생하여 메모리초과(런타임에러)가 발생한다.
# 예외케이스 : n = 885733, k = 3, result = 1
def make_prime_numbers(n):
    prime_numbers = [True] * (n + 1)
    prime_numbers[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if prime_numbers[num]:
            for i in range(num ** 2, n + 1, num):
                prime_numbers[i] = False
    return prime_numbers

def solution(n, k):
    # 1. k진수로 바꾸기
    k_strings = ""
    while n >= k:
        a, b = divmod(n, k)
        k_strings = str(b) + k_strings
        n = a
    k_strings = str(n) + k_strings

    # 2. 소수찾기
    numbers = sorted([int(x) for x in k_strings.split("0") if x != ""])
    # 3-1. 조건에 맞는 숫자가 없다면 바로 리턴
    if not numbers:
        return 0

    MAX = numbers[-1]
    prime_numbers = make_prime_numbers(MAX)
    
    result = 0
    for number in numbers:
        if prime_numbers[number]:
            result += 1
    
    return result
# 정확성 테스트
# 테스트 1 〉 실패 (런타임 에러)
# 테스트 2 〉 통과 (0.24ms, 10.4MB)
# 테스트 3 〉 통과 (0.03ms, 10.3MB)
# 테스트 4 〉 통과 (0.09ms, 10.3MB)
# 테스트 5 〉 통과 (0.04ms, 10.3MB)
# 테스트 6 〉 통과 (0.03ms, 10.4MB)
# 테스트 7 〉 통과 (0.05ms, 10.3MB)
# 테스트 8 〉 통과 (0.03ms, 10.3MB)
# 테스트 9 〉 통과 (0.03ms, 10.5MB)
# 테스트 10 〉 통과 (0.03ms, 10.3MB)
# 테스트 11 〉 실패 (런타임 에러)
# 테스트 12 〉 통과 (0.07ms, 10.3MB)
# 테스트 13 〉 통과 (0.09ms, 10.4MB)
# 테스트 14 〉 통과 (0.03ms, 10.3MB)
# 테스트 15 〉 통과 (0.03ms, 10.3MB)
# 테스트 16 〉 통과 (0.04ms, 10.4MB)


# 에라토스테네스의 체가 아닌 소수판별 알고리즘
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0: 
            return False
        i += 1
    return True

def convert_number(number, k):
    string = ""
    while number:
        string = str(number % k) + string
        number //= k
    return string

def solution(n, k):
    string = convert_number(n, k)

    numbers = [int(x) for x in string.split("0") if x != ""]

    result = 0
    for number in numbers:
        if is_prime(number):
            result += 1
    
    return result
"""
정확성 테스트
테스트 1 〉 통과 (142.11ms, 10.2MB)
테스트 2 〉 통과 (0.04ms, 10.4MB)
테스트 3 〉 통과 (0.02ms, 10.3MB)
테스트 4 〉 통과 (0.03ms, 10.3MB)
테스트 5 〉 통과 (0.03ms, 10.3MB)
테스트 6 〉 통과 (0.03ms, 10.4MB)
테스트 7 〉 통과 (0.03ms, 10.3MB)
테스트 8 〉 통과 (0.03ms, 10.2MB)
테스트 9 〉 통과 (0.03ms, 10.4MB)
테스트 10 〉 통과 (0.03ms, 10.4MB)
테스트 11 〉 통과 (0.04ms, 10.2MB)
테스트 12 〉 통과 (0.02ms, 10.2MB)
테스트 13 〉 통과 (0.03ms, 10.4MB)
테스트 14 〉 통과 (0.02ms, 10.3MB)
테스트 15 〉 통과 (0.03ms, 10.4MB)
테스트 16 〉 통과 (0.03ms, 10.3MB)
"""