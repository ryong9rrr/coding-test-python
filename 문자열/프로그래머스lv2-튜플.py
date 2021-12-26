# stack과 Counter 모듈을 이용한 풀이
from collections import Counter
def solution(s):
    result = []
    stack = []
    for char in s:
        if char.isdigit():
            stack.append(char)
        if char == "," or char == "}":
            number = ""
            while stack:
                number = stack.pop() + number
            if number:
                result.append(int(number))
    n = len(Counter(result))
    return [x[0] for x in list(Counter(result).most_common(n))]

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.13ms, 10.4MB)
테스트 5 〉	통과 (0.54ms, 10.3MB)
테스트 6 〉	통과 (1.12ms, 10.4MB)
테스트 7 〉	통과 (20.23ms, 11.2MB)
테스트 8 〉	통과 (65.52ms, 12.9MB)
테스트 9 〉	통과 (43.07ms, 11.5MB)
테스트 10 〉	통과 (65.97ms, 12.8MB)
테스트 11 〉	통과 (101.35ms, 14.2MB)
테스트 12 〉	통과 (178.05ms, 17.2MB)
테스트 13 〉	통과 (175.54ms, 17.1MB)
테스트 14 〉	통과 (190.26ms, 17.7MB)
테스트 15 〉	통과 (0.04ms, 10.4MB)
"""

# 그런데 생각해보면 굳이 stack을 사용할 필요가 없잖아?
# + Counter를 변수에 담아서 조금 더 최적화, most_common 사용안하고 정렬
from collections import Counter
def solution(s):
    result = []
    number = ""
    for char in s:
        if char.isdigit():
            number += char
        if char == "," or char == "}":
            if number:
                result.append(int(number))
                number = ""
    counts = Counter(result)
    return [x[0] for x in sorted(counts.items(), key = lambda x: x[1], reverse = True)]

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.09ms, 10.4MB)
테스트 5 〉	통과 (0.34ms, 10.4MB)
테스트 6 〉	통과 (0.80ms, 10.4MB)
테스트 7 〉	통과 (12.84ms, 11.1MB)
테스트 8 〉	통과 (41.68ms, 12.9MB)
테스트 9 〉	통과 (21.67ms, 11.4MB)
테스트 10 〉	통과 (42.50ms, 12.9MB)
테스트 11 〉	통과 (63.16ms, 14.1MB)
테스트 12 〉	통과 (109.59ms, 16.6MB)
테스트 13 〉	통과 (102.82ms, 16.4MB)
테스트 14 〉	통과 (105.46ms, 16.5MB)
테스트 15 〉	통과 (0.04ms, 10.4MB)
"""