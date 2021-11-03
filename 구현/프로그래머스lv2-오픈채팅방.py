#정규표현식 폴더에서는 정규표현식을 썼었지만... 로직자체가 너무 비효율적이었음.
# 딱히 다른점은 많이 없긴하지만 시간을 엄청 개선시킨방법
from collections import defaultdict
def solution(record):
    # id - nickname dictionary 생성
    dic = defaultdict(str)
    for rec in record:
        r = rec.split(" ")
        if r[0] != "Leave":
            [_, _id, nickname] = r
            dic[_id] = nickname
            
    result = []
    for rec in record:
        r = rec.split(" ")
        _id = r[1]
        if r[0] == "Leave":
            result.append(f"{dic[_id]}님이 나갔습니다.")
        elif r[0] == "Enter":
            result.append(f"{dic[_id]}님이 들어왔습니다.")
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.4MB)
테스트 5 〉	통과 (1.01ms, 10.4MB)
테스트 6 〉	통과 (1.01ms, 10.6MB)
테스트 7 〉	통과 (0.92ms, 10.4MB)
테스트 8 〉	통과 (0.74ms, 10.4MB)
테스트 9 〉	통과 (1.02ms, 10.6MB)
테스트 10 〉	통과 (0.78ms, 10.4MB)
테스트 11 〉	통과 (0.44ms, 10.4MB)
테스트 12 〉	통과 (0.42ms, 10.5MB)
테스트 13 〉	통과 (0.74ms, 10.4MB)
테스트 14 〉	통과 (0.97ms, 10.6MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.11ms, 10.3MB)
테스트 18 〉	통과 (0.07ms, 10.2MB)
테스트 19 〉	통과 (1.15ms, 10.6MB)
테스트 20 〉	통과 (0.94ms, 10.4MB)
테스트 21 〉	통과 (0.61ms, 10.4MB)
테스트 22 〉	통과 (0.89ms, 10.4MB)
테스트 23 〉	통과 (0.71ms, 10.7MB)
테스트 24 〉	통과 (0.69ms, 10.5MB)
테스트 25 〉	통과 (79.96ms, 47.5MB)
테스트 26 〉	통과 (86.86ms, 50.1MB)
테스트 27 〉	통과 (119.28ms, 50MB)
테스트 28 〉	통과 (115.35ms, 51.5MB)
테스트 29 〉	통과 (99.68ms, 51.6MB)
테스트 30 〉	통과 (72.88ms, 44.5MB)
테스트 31 〉	통과 (86.61ms, 52MB)
테스트 32 〉	통과 (64.73ms, 47.5MB)
"""