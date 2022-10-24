"""
내 위로 몇명이 있는지? 를 찾으면 됨.
"""
from collections import defaultdict
def solution(score):
    table = defaultdict(int)
    for a, b in score:
        table[(a + b) / 2] += 1
    
    ranks = defaultdict(int)
    acc = 0
    for _score in sorted(table.keys(), reverse = True):
        if acc == 0:
            ranks[_score] = 1
        else:
            ranks[_score] = acc + 1
        acc += table[_score]
    
    result = []
    for a, b, in score:
        result.append(ranks[(a + b) / 2])
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 9.96MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
"""