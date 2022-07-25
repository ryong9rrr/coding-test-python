from functools import reduce
def solution(n, m):
    x, y = n, m
    gcd = [1]
    if n > m:
        n, m = m, n
    
    i = 2
    while(i <= n) :
        if(n % i == 0 and m % i == 0) :
            gcd.append(i)
            n //= i
            m //= i
        else :
            i += 1
    
    GCD = reduce(lambda a, b: a * b, gcd)
    LCM = (x * y) // GCD
    return [GCD, LCM]

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
"""

# math.gcd 사용
import math
def solution(n, m):
    GCD = math.gcd(n, m)
    LCM = n * m // GCD
    return [GCD, LCM]
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)

"""