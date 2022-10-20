# 2022 8월 프로그래머스 모의테스트 2회 1번문제
from itertools import combinations
def solution(number):
    count = 0
    for array in list(combinations(number, 3)):
        if sum(array) == 0:
            count += 1

    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.1MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.1MB)
테스트 8 〉	통과 (0.08ms, 10.1MB)
테스트 9 〉	통과 (0.09ms, 10.1MB)
테스트 10 〉	통과 (0.05ms, 10MB)
테스트 11 〉	통과 (0.04ms, 10.1MB)
테스트 12 〉	통과 (0.08ms, 10.1MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
"""