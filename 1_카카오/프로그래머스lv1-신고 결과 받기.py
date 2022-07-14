# 너무 오랜만에 풀었나...
def solution(id_list, report, k):
    table = {}
    banned = {}
    
    # 데이터 테이블 초기화(배열 이용)
    for user in id_list:
        banned[user] = 0
        table[user] = []
    
    # 신고 현황 테이블 갱신
    for info in report:
        user, r_user = info.split(" ")
        if not r_user in table[user]:
            table[user].append(r_user)
            banned[r_user] += 1
    
    result = []
    for user in id_list:
        count = 0
        for r_user in table[user]:
            if banned[r_user] >= k:
                count += 1
        result.append(count)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (496.39ms, 37.8MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (1.15ms, 10.5MB)
테스트 7 〉	통과 (2.93ms, 10.6MB)
테스트 8 〉	통과 (5.48ms, 10.9MB)
테스트 9 〉	통과 (203.94ms, 23.1MB)
테스트 10 〉	통과 (215.09ms, 23.1MB)
테스트 11 〉	통과 (469.29ms, 37.7MB)
테스트 12 〉	통과 (0.22ms, 10.3MB)
테스트 13 〉	통과 (0.21ms, 10.2MB)
테스트 14 〉	통과 (103.04ms, 22.1MB)
테스트 15 〉	통과 (244.52ms, 31.1MB)
테스트 16 〉	통과 (0.13ms, 10.3MB)
테스트 17 〉	통과 (0.21ms, 10.3MB)
테스트 18 〉	통과 (0.34ms, 10.4MB)
테스트 19 〉	통과 (0.60ms, 10.4MB)
테스트 20 〉	통과 (97.84ms, 22MB)
테스트 21 〉	통과 (232.69ms, 30.7MB)
테스트 22 〉	통과 (0.00ms, 10.1MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (0.00ms, 10.1MB)
"""

# set, defaultdict 이용(맨 처음 풀이 참고)
from collections import defaultdict
def solution(id_list, report, k):
    table = defaultdict(set)
    banned = defaultdict(int)
    
    # 신고 현황 테이블 갱신(set 이용)
    for info in report:
        user, r_user = info.split(" ")
        table[user].add(r_user)
    
    # 신고당한사람 테이블 갱신
    for user in table:
        for r_user in table[user]:
            banned[r_user] += 1
    
    # 결과
    result = []
    for user in id_list:
        count = 0
        for r_user in table[user]:
            if banned[r_user] >= k:
                count += 1
        result.append(count)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.87ms, 10.1MB)
테스트 2 〉	통과 (0.87ms, 10.1MB)
테스트 3 〉	통과 (153.71ms, 44.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.94ms, 10.4MB)
테스트 7 〉	통과 (1.92ms, 10.6MB)
테스트 8 〉	통과 (3.57ms, 10.9MB)
테스트 9 〉	통과 (67.97ms, 26.5MB)
테스트 10 〉	통과 (102.89ms, 26.3MB)
테스트 11 〉	통과 (182.49ms, 44.3MB)
테스트 12 〉	통과 (0.31ms, 10.3MB)
테스트 13 〉	통과 (0.27ms, 10.3MB)
테스트 14 〉	통과 (72.44ms, 23.5MB)
테스트 15 〉	통과 (142.41ms, 38.5MB)
테스트 16 〉	통과 (0.16ms, 10.1MB)
테스트 17 〉	통과 (0.39ms, 10.2MB)
테스트 18 〉	통과 (0.42ms, 10.3MB)
테스트 19 〉	통과 (0.71ms, 10.2MB)
테스트 20 〉	통과 (63.85ms, 23.6MB)
테스트 21 〉	통과 (150.28ms, 38.5MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
"""