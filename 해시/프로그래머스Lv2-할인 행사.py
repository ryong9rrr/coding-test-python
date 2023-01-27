# 2022 8월 프로그래머스 모의테스트 1회 2번문제
from collections import Counter
def solution(want, number, discount):
    N = len(discount)
    M = len(want)
    
    def validate(counter):
        return all(counter[want[i]] >= number[i] for i in range(M))
    
    result = 0
    for day in range(N - 10 + 1):
        counter = Counter(discount[day : day + 10])
        if validate(counter):
            result += 1
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (22.61ms, 10.6MB)
테스트 2 〉	통과 (166.25ms, 14.8MB)
테스트 3 〉	통과 (52.72ms, 11MB)
테스트 4 〉	통과 (272.96ms, 15.8MB)
테스트 5 〉	통과 (93.19ms, 12.9MB)
테스트 6 〉	통과 (16.97ms, 10.4MB)
테스트 7 〉	통과 (79.70ms, 11.4MB)
테스트 8 〉	통과 (333.93ms, 17.4MB)
테스트 9 〉	통과 (64.59ms, 11.1MB)
테스트 10 〉	통과 (163.73ms, 13.8MB)
테스트 11 〉	통과 (39.78ms, 10.7MB)
테스트 12 〉	통과 (0.11ms, 10.2MB)
"""