# 파이썬 내장함수 hash() 사용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.38ms, 10.3MB)
테스트 4 〉	통과 (0.78ms, 10.4MB)
테스트 5 〉	통과 (0.81ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (26.53ms, 23.9MB)
테스트 2 〉	통과 (39.62ms, 28.4MB)
테스트 3 〉	통과 (47.53ms, 31.4MB)
테스트 4 〉	통과 (55.91ms, 37.7MB)
테스트 5 〉	통과 (56.95ms, 37.8MB)
"""

# 딕셔너리 사용
from collections import defaultdict
def solution(participant, completion):
    obj = defaultdict(int)
    for i, v in enumerate(completion):
        obj[v] += 1
        
    for i, v in enumerate(participant):
        if obj[v] == 0 :
            return v
        obj[v] -= 1

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.14ms, 10.3MB)
테스트 4 〉	통과 (0.34ms, 10.4MB)
테스트 5 〉	통과 (0.31ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (19.55ms, 21.7MB)
테스트 2 〉	통과 (36.36ms, 25.2MB)
테스트 3 〉	통과 (38.18ms, 27.6MB)
테스트 4 〉	통과 (39.76ms, 33.9MB)
테스트 5 〉	통과 (66.50ms, 34MB)
"""