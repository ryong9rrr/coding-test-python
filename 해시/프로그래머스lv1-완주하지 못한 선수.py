# 정석
def solution(participant, completion):
    people = {}

    for name in completion:
        if name not in people:
            people[name] = 0
        people[name] += 1
    
    for name in participant:
        if name not in people or people[name] == 0:
            return name
        people[name] -= 1
    
    return None
"""
정확성 테스트
테스트 1 〉 통과 (0.01ms, 10.2MB)
테스트 2 〉 통과 (0.01ms, 10.1MB)
테스트 3 〉 통과 (0.19ms, 10.3MB)
테스트 4 〉 통과 (0.30ms, 10.4MB)
테스트 5 〉 통과 (0.25ms, 10.2MB)
효율성 테스트
테스트 1 〉 통과 (15.40ms, 21.6MB)
테스트 2 〉 통과 (31.21ms, 25.2MB)
테스트 3 〉 통과 (29.19ms, 27.4MB)
테스트 4 〉 통과 (34.54ms, 33.9MB)
테스트 5 〉 통과 (53.38ms, 33.9MB)
"""

# defaultdict
from collections import defaultdict
def solution(participant, completion):
    people = defaultdict(int)
    
    for name in completion:
        people[name] += 1
    
    for name in participant:
        if name not in people or people[name] == 0:
            return name
        people[name] -= 1

"""
정확성 테스트
테스트 1 〉 통과 (0.01ms, 10.1MB)
테스트 2 〉 통과 (0.02ms, 10.2MB)
테스트 3 〉 통과 (0.30ms, 10.1MB)
테스트 4 〉 통과 (0.32ms, 10.4MB)
테스트 5 〉 통과 (0.49ms, 10.3MB)
효율성 테스트
테스트 1 〉 통과 (19.10ms, 21.8MB)
테스트 2 〉 통과 (35.45ms, 25.2MB)
테스트 3 〉 통과 (35.42ms, 27.5MB)
테스트 4 〉 통과 (32.98ms, 33.9MB)
테스트 5 〉 통과 (56.26ms, 33.9MB)
"""

# Counter 사용
from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    
    for name in p.keys():
        if not c[name]:
            return name
        c[name] -= p[name]
        if c[name] < 0:
            return name

"""
정확성 테스트
테스트 1 〉 통과 (0.04ms, 9.98MB)
테스트 2 〉 통과 (0.04ms, 10.1MB)
테스트 3 〉 통과 (0.17ms, 10.3MB)
테스트 4 〉 통과 (0.45ms, 10.3MB)
테스트 5 〉 통과 (0.26ms, 10.5MB)
효율성 테스트
테스트 1 〉 통과 (21.29ms, 24.2MB)
테스트 2 〉 통과 (46.22ms, 27.7MB)
테스트 3 〉 통과 (37.52ms, 30.1MB)
테스트 4 〉 통과 (39.23ms, 39MB)
테스트 5 〉 통과 (34.49ms, 38.9MB)
"""