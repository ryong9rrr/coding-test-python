def solution(n):
    # 0 부터 n까지 소수의 배열을 만들어내는 함수
    def makePrimeNumbers(n:int)->list:
        prime_numbers = [True] * (n + 1)
        prime_numbers[0:2] = [False, False]
        for num in range(2, int(n * 0.5) + 1):
            if prime_numbers[num]:
                for i in range(num ** 2, n + 1, num):
                    prime_numbers[i] = False
        return prime_numbers

    prime = makePrimeNumbers(n)

    return prime[:n + 1].count(True)

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.18ms, 10.4MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.97ms, 10.3MB)
테스트 7 〉	통과 (0.54ms, 10.3MB)
테스트 8 〉	통과 (1.17ms, 10.2MB)
테스트 9 〉	통과 (1.14ms, 10.3MB)
테스트 10 〉	통과 (35.11ms, 14.3MB)
테스트 11 〉	통과 (114.53ms, 23.5MB)
테스트 12 〉	통과 (39.41ms, 14.7MB)
효율성  테스트
테스트 1 〉	통과 (128.41ms, 24.3MB)
테스트 2 〉	통과 (121.79ms, 23.7MB)
테스트 3 〉	통과 (125.39ms, 24.2MB)
테스트 4 〉	통과 (125.85ms, 24.1MB)
"""