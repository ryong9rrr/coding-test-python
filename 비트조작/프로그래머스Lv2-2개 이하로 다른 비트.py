def f(number):
    n = number + 1
    while True:
        XOR = bin(number ^ n)[2:]
        cnt = XOR.count("1")
        if 1 <= cnt and cnt <= 2:
            return n
        n += 1

def solution(numbers):
    return [f(x) for x in numbers]
"""
정확성 테스트
테스트 1 〉 통과 (0.94ms, 10.3MB)
테스트 2 〉 통과 (153.36ms, 22.8MB)
테스트 3 〉 통과 (0.21ms, 10.2MB)
테스트 4 〉 통과 (0.86ms, 10.5MB)
테스트 5 〉 통과 (2.78ms, 10.3MB)
테스트 6 〉 통과 (3.26ms, 10.4MB)
테스트 7 〉 통과 (209.70ms, 23.8MB)
테스트 8 〉 통과 (122.11ms, 23.4MB)
테스트 9 〉 통과 (173.10ms, 23MB)
테스트 10 〉 실패 (시간 초과)
테스트 11 〉 실패 (시간 초과)
"""

# 2진수의 특징을 이용한 규칙찾기
def f(n):
    if n % 2 == 0:
        return n + 1
    else:
        bin_s = "0" + bin(n)[2:]
        i = bin_s.rfind("0")
        bin_arr = list(bin_s)
        bin_arr[i], bin_arr[i + 1] = "1", "0"
        return int("".join(bin_arr), 2)

def solution(numbers):
    return [f(x) for x in numbers]
"""
정확성 테스트
테스트 1 〉 통과 (0.61ms, 10.4MB)
테스트 2 〉 통과 (70.73ms, 22.8MB)
테스트 3 〉 통과 (0.12ms, 10.4MB)
테스트 4 〉 통과 (0.51ms, 10.3MB)
테스트 5 〉 통과 (0.64ms, 10.3MB)
테스트 6 〉 통과 (0.88ms, 10.5MB)
테스트 7 〉 통과 (80.02ms, 22.3MB)
테스트 8 〉 통과 (77.19ms, 22MB)
테스트 9 〉 통과 (73.85ms, 21.8MB)
테스트 10 〉 통과 (142.84ms, 23.8MB)
테스트 11 〉 통과 (139.72ms, 23.8MB)
"""