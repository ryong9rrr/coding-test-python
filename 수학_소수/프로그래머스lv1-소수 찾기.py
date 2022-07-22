def make_prime_numbers(n:int)->list:
    prime_numbers = [True] * (n + 1)
    prime_numbers[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if prime_numbers[num]:
            for i in range(num ** 2, n + 1, num):
                prime_numbers[i] = False
    return prime_numbers

def solution(n):
    prime_numbers = make_prime_numbers(n)
    return prime_numbers.count(True)
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.11ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.3MB)
테스트 6 〉	통과 (0.96ms, 10MB)
테스트 7 〉	통과 (0.30ms, 9.98MB)
테스트 8 〉	통과 (0.71ms, 10.3MB)
테스트 9 〉	통과 (1.12ms, 10.4MB)
테스트 10 〉	통과 (34.23ms, 12.1MB)
테스트 11 〉	통과 (111.20ms, 16.7MB)
테스트 12 〉	통과 (38.34ms, 12.4MB)
효율성  테스트
테스트 1 〉	통과 (127.47ms, 17.1MB)
테스트 2 〉	통과 (115.78ms, 16.8MB)
테스트 3 〉	통과 (128.21ms, 17MB)
테스트 4 〉	통과 (118.30ms, 17.1MB)
"""