# 파이썬 내장함수 hash() 사용
def solution(participant, completion):
    dic = {}
    total = 0
    for p in participant:
        dic[hash(p)] = p
        total += hash(p)
    
    for c in completion:
        total -= hash(c)
    
    return dic[total]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.21ms, 10.2MB)
테스트 4 〉	통과 (0.38ms, 10.4MB)
테스트 5 〉	통과 (0.44ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (23.57ms, 23.9MB)
테스트 2 〉	통과 (33.55ms, 28.5MB)
테스트 3 〉	통과 (39.54ms, 31.4MB)
테스트 4 〉	통과 (49.67ms, 37.8MB)
테스트 5 〉	통과 (44.75ms, 37.8MB)
"""

# 딕셔너리 사용
def solution(participant, completion):
    com = {}
    for c in completion:
        if not c in com:
            com[c] = 1
        else:
            com[c] += 1
    
    for p in participant:
        if not p in com or not com[p]:
            return p
        com[p] -= 1

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.09ms, 10.4MB)
테스트 4 〉	통과 (0.24ms, 10.4MB)
테스트 5 〉	통과 (0.21ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (14.13ms, 21.7MB)
테스트 2 〉	통과 (30.57ms, 25.2MB)
테스트 3 〉	통과 (23.33ms, 27.6MB)
테스트 4 〉	통과 (28.91ms, 34MB)
테스트 5 〉	통과 (47.71ms, 34MB)
"""

# 딕셔너리(defaultdict) 사용
from collections import defaultdict
def solution(participant, completion):
    com = defaultdict(int)
    for c in completion:
        com[c] += 1
    
    for p in participant:
        com[p] -= 1
        if com[p] < 0:
            return p

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.23ms, 10.3MB)
테스트 4 〉	통과 (0.33ms, 10.5MB)
테스트 5 〉	통과 (0.48ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (17.47ms, 21.8MB)
테스트 2 〉	통과 (36.04ms, 25.3MB)
테스트 3 〉	통과 (29.70ms, 27.6MB)
테스트 4 〉	통과 (38.04ms, 34MB)
테스트 5 〉	통과 (52.58ms, 34MB)
"""

# Counter 사용

from collections import Counter
def solution(participant, completion):
    part = Counter(participant)
    com = Counter(completion)
    
    for key in part.keys():
        if not com[key]:
            return key
        com[key] -= part[key]
        if com[key] < 0:
            return key

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.18ms, 10.4MB)
테스트 4 〉	통과 (0.67ms, 10.4MB)
테스트 5 〉	통과 (0.28ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (20.80ms, 24.4MB)
테스트 2 〉	통과 (42.82ms, 27.8MB)
테스트 3 〉	통과 (41.13ms, 30.2MB)
테스트 4 〉	통과 (45.21ms, 39MB)
테스트 5 〉	통과 (31.45ms, 38.9MB)
"""