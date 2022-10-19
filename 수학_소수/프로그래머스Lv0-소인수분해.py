def make_primes(n:int)->list:
    primes = [True] * (n + 1)
    primes[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if primes[num]:
            for i in range(num ** 2, n + 1, num):
                primes[i] = False
    return primes

def solution(n):
    primes = make_primes(n)
    prime_numbers = [x for x in range(2, n + 1) if primes[x]]
    
    result = []
    for number in prime_numbers:
        if n % number == 0:
            result.append(number)
        while n > 1 and n % number == 0:
            n //= number
        if n == 1:
            break
    return result
"""
정확성  테스트
테스트 1 〉	통과 (2.67ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.85ms, 10.1MB)
테스트 6 〉	통과 (0.19ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.13ms, 10.4MB)
테스트 9 〉	통과 (2.76ms, 10.1MB)
테스트 10 〉	통과 (0.56ms, 10.3MB)
테스트 11 〉	통과 (1.00ms, 10.2MB)
테스트 12 〉	통과 (1.63ms, 10.2MB)
테스트 13 〉	통과 (2.52ms, 10.1MB)
테스트 14 〉	통과 (1.51ms, 10.1MB)
테스트 15 〉	통과 (1.18ms, 10.2MB)
테스트 16 〉	통과 (1.19ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.02ms, 9.96MB)
테스트 24 〉	통과 (0.65ms, 10.2MB)
"""