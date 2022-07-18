def solution(nums):
    def makePrimeNumbers(n:int)->list:
        prime_numbers = [True] * (n + 1)
        prime_numbers[0:2] = [False, False]
        for num in range(2, int(n * 0.5) + 1):
            if prime_numbers[num]:
                for i in range(num ** 2, n + 1, num):
                    prime_numbers[i] = False
        return prime_numbers
    
    n = sum(sorted(nums)[-3:])
    prime = makePrimeNumbers(n)
    
    result = 0
    leng = len(nums)
    # 조합찾기
    for i in range(0, leng - 2) :
        for j in range(i + 1, leng - 1) :
            for k in range(j + 1, leng) :
                a, b, c = nums[i], nums[j], nums[k]
                if prime[a + b + c] :
                    result += 1
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.44ms, 10.3MB)
테스트 2 〉	통과 (1.04ms, 10.3MB)
테스트 3 〉	통과 (0.21ms, 10.3MB)
테스트 4 〉	통과 (0.12ms, 10.3MB)
테스트 5 〉	통과 (0.69ms, 10.3MB)
테스트 6 〉	통과 (1.23ms, 10.2MB)
테스트 7 〉	통과 (0.25ms, 10.3MB)
테스트 8 〉	통과 (3.43ms, 10.2MB)
테스트 9 〉	통과 (0.28ms, 10.3MB)
테스트 10 〉	통과 (2.68ms, 10.3MB)
테스트 11 〉	통과 (0.08ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.04ms, 10.3MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
테스트 16 〉	통과 (2.47ms, 10.3MB)
테스트 17 〉	통과 (3.00ms, 10.3MB)
테스트 18 〉	통과 (0.47ms, 10.3MB)
테스트 19 〉	통과 (0.29ms, 10.3MB)
테스트 20 〉	통과 (3.88ms, 10.3MB)
테스트 21 〉	통과 (5.37ms, 10.2MB)
테스트 22 〉	통과 (1.61ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (2.79ms, 10.3MB)
테스트 25 〉	통과 (2.35ms, 10.3MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
"""

from itertools import combinations
def make_prime_numbers(n:int)->list:
    prime_numbers = [True] * (n + 1)
    prime_numbers[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if prime_numbers[num]:
            for i in range(num ** 2, n + 1, num):
                prime_numbers[i] = False
    return prime_numbers

def solution(nums):
    RANGE = sum(sorted(nums, reverse = True)[0:3])
    prime_numbers = make_prime_numbers(RANGE)
    total_numbers = [sum(numbers) for numbers in list(combinations(nums, 3))]
    
    result = 0
    for total in total_numbers:
        if prime_numbers[total]:
            result += 1
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.69ms, 10.3MB)
테스트 2 〉	통과 (0.94ms, 10.6MB)
테스트 3 〉	통과 (0.19ms, 10.4MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (1.96ms, 10.3MB)
테스트 6 〉	통과 (1.71ms, 10.5MB)
테스트 7 〉	통과 (0.14ms, 10.3MB)
테스트 8 〉	통과 (3.95ms, 11.6MB)
테스트 9 〉	통과 (0.37ms, 10.3MB)
테스트 10 〉	통과 (3.73ms, 11.2MB)
테스트 11 〉	통과 (0.07ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.1MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (4.10ms, 11.6MB)
테스트 17 〉	통과 (5.18ms, 11.9MB)
테스트 18 〉	통과 (0.31ms, 10.2MB)
테스트 19 〉	통과 (0.31ms, 10.3MB)
테스트 20 〉	통과 (5.75ms, 12.1MB)
테스트 21 〉	통과 (4.91ms, 11.8MB)
테스트 22 〉	통과 (1.14ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (4.09ms, 11.8MB)
테스트 25 〉	통과 (4.09ms, 11.6MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
"""