from collections import defaultdict
def make_primes(n:int)->list:
    primes = [True] * (n + 1)
    primes[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if primes[num]:
            for i in range(num ** 2, n + 1, num):
                primes[i] = False
    return primes

def make_prime_factorization(n):
    primes = make_primes(n)
    prime_numbers = [x for x in range(2, n + 1) if primes[x]]
    result = defaultdict(int)
    for number in prime_numbers:
        while n % number == 0 and n > 1:
            result[number] += 1
            n //= number
        if n == 1:
            break
    return result

def solution(a, b):
    molecule = make_prime_factorization(a)
    denominator = make_prime_factorization(b)
    
    # 분모 약분
    for key, value in molecule.items():
        if key in denominator:
            denominator[key] = max(0, denominator[key] - value)
    
    # 유한 소수 판별
    for key, value in denominator.items():
        if key == 2 or key == 5:
            continue
        if value > 0:
            return 2
    return 1
"""
정확성  테스트
테스트 1 〉	통과 (0.12ms, 10.1MB)
테스트 2 〉	통과 (0.19ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.11ms, 10.1MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.15ms, 10.3MB)
테스트 8 〉	통과 (0.12ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.4MB)
테스트 10 〉	통과 (0.26ms, 10.1MB)
테스트 11 〉	통과 (0.05ms, 10.3MB)
테스트 12 〉	통과 (0.16ms, 10MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
"""