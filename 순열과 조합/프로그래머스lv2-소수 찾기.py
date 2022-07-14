from itertools import permutations
# 입력받은 n까지 원소가 True나 False인 소수배열을 만들어내는 함수
def makePrimeNumbers(n:int)->list:
        prime_numbers = [True] * (n + 1)
        prime_numbers[0:2] = [False, False]
        for num in range(2, int(n * 0.5) + 1):
            if prime_numbers[num]:
                for i in range(num ** 2, n + 1, num):
                    prime_numbers[i] = False
        return prime_numbers

def solution(numbers):
    # 가장 큰 숫자만큼 소수 배열을 생성
    n = int("".join(sorted(numbers, reverse = True)))
    primeNumbers = makePrimeNumbers(n)
    
    # 만들어낼 수 있는 모든 숫자찾기 (순열)
    # 중복 값은 제외하기 위해 set.add()
    nums = set([])
    for i in range(1, len(numbers) + 1):
        for num in list(permutations(numbers, i)):
            nums.add(int("".join(num)))
    
    result = 0
    for num in nums:
        if primeNumbers[num]:
            result += 1
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.39ms, 10.5MB)
테스트 2 〉	통과 (86.66ms, 15.5MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (42.57ms, 12.6MB)
테스트 5 〉	통과 (674.78ms, 36.7MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.38ms, 10.4MB)
테스트 8 〉	통과 (1104.28ms, 53.4MB)
테스트 9 〉	통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (128.07ms, 18.1MB)
테스트 11 〉	통과 (11.89ms, 10.9MB)
테스트 12 〉	통과 (6.06ms, 10.5MB)
"""