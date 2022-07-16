def solution(N, stages):
    users_num = len(stages)
    
    fails = []
    for i in range(1, N+1) :
        temp = 0
        for stage in stages :
            if stage == i :
                temp += 1
        if users_num != 0 :
            fails.append( [i, temp/users_num] )
        else :
            fails.append( [i, 0] )
        users_num = users_num - temp
    
    fails = sorted(fails, key= lambda x : x[1], reverse=True)
    
    result = []
    for fail in fails :
        result.append( fail[0] )
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (1.22ms, 10.2MB)
테스트 3 〉	통과 (121.83ms, 10.4MB)
테스트 4 〉	통과 (574.48ms, 10.9MB)
테스트 5 〉	통과 (2317.69ms, 15.1MB)
테스트 6 〉	통과 (2.78ms, 10.2MB)
테스트 7 〉	통과 (24.59ms, 10.3MB)
테스트 8 〉	통과 (576.95ms, 10.9MB)
테스트 9 〉	통과 (2472.79ms, 15MB)
테스트 10 〉	통과 (245.64ms, 10.9MB)
테스트 11 〉	통과 (579.60ms, 10.9MB)
테스트 12 〉	통과 (360.37ms, 11.3MB)
테스트 13 〉	통과 (804.92ms, 11.4MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (21.52ms, 10.7MB)
테스트 16 〉	통과 (11.20ms, 10.5MB)
테스트 17 〉	통과 (25.63ms, 10.5MB)
테스트 18 〉	통과 (13.31ms, 10.4MB)
테스트 19 〉	통과 (2.67ms, 10.3MB)
테스트 20 〉	통과 (19.27ms, 10.3MB)
테스트 21 〉	통과 (36.93ms, 10.9MB)
테스트 22 〉	통과 (2154.83ms, 18.5MB)
테스트 23 〉	통과 (31.63ms, 11.6MB)
테스트 24 〉	통과 (111.66ms, 11.7MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
"""

from collections import defaultdict
def solution(N, stages):
    n = len(stages)
    #실패율->스테이지에 도달했지만 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어수
    info = defaultdict(int)
    for stage in stages:
        info[stage] += 1
    
    d = defaultdict(float)
    
    for stage in range(1, N + 1):
        if info[stage] and n != 0:
            d[stage] = info[stage] / n
        else:
            d[stage] = 0
        n -= info[stage]
    key_sorted = sorted(d.items(), key = lambda x : x[1], reverse = True)
    result = []
    for i in key_sorted:
        result.append(i[0])
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (1.06ms, 10.6MB)
테스트 4 〉	통과 (6.28ms, 10.9MB)
테스트 5 〉	통과 (17.17ms, 15MB)
테스트 6 〉	통과 (0.12ms, 10.2MB)
테스트 7 〉	통과 (0.64ms, 10.3MB)
테스트 8 〉	통과 (6.75ms, 10.9MB)
테스트 9 〉	통과 (17.58ms, 15.1MB)
테스트 10 〉	통과 (7.64ms, 10.9MB)
테스트 11 〉	통과 (7.06ms, 10.9MB)
테스트 12 〉	통과 (10.36ms, 11.5MB)
테스트 13 〉	통과 (11.16ms, 11.4MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (4.59ms, 10.6MB)
테스트 16 〉	통과 (2.35ms, 10.4MB)
테스트 17 〉	통과 (4.83ms, 10.7MB)
테스트 18 〉	통과 (2.28ms, 10.4MB)
테스트 19 〉	통과 (0.45ms, 10.3MB)
테스트 20 〉	통과 (3.21ms, 10.3MB)
테스트 21 〉	통과 (7.02ms, 11MB)
테스트 22 〉	통과 (18.27ms, 18.3MB)
테스트 23 〉	통과 (13.03ms, 11.6MB)
테스트 24 〉	통과 (12.73ms, 11.6MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.3MB)
"""

# 2022년 7월 풀이
from collections import defaultdict
def solution(N, stages):
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    # 스테이지의 개수는 최대 500
    # stages의 길이 = 사용자의 수(최대 20만)
    failure_table = defaultdict(int)
    for stage in stages:
        if stage <= N:
            failure_table[stage] += 1
        
    all_users_length = len(stages)
    for stage in range(1, N + 1):
        users_length = failure_table[stage]
        if users_length == 0 or all_users_length == 0:
            failure_table[stage] = 0
        else:
            failure_table[stage] = users_length / all_users_length
        all_users_length -= users_length
        if all_users_length < 0:
            raise Exception("전체 유저 수가 0보다 작아짐")
    
    result = sorted(
                failure_table.items(),
                key = lambda x: (x[1], -x[0]),
                reverse = True)
    
    return [key for key, value in result]
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.1MB)
테스트 3 〉	통과 (1.31ms, 10.4MB)
테스트 4 〉	통과 (7.90ms, 10.7MB)
테스트 5 〉	통과 (20.63ms, 14.9MB)
테스트 6 〉	통과 (0.25ms, 10.1MB)
테스트 7 〉	통과 (0.77ms, 10.3MB)
테스트 8 〉	통과 (7.77ms, 10.8MB)
테스트 9 〉	통과 (20.86ms, 15.1MB)
테스트 10 〉	통과 (8.01ms, 10.7MB)
테스트 11 〉	통과 (11.78ms, 10.7MB)
테스트 12 〉	통과 (12.28ms, 11.2MB)
테스트 13 〉	통과 (13.32ms, 11.4MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (6.97ms, 10.7MB)
테스트 16 〉	통과 (2.86ms, 10.2MB)
테스트 17 〉	통과 (5.87ms, 10.5MB)
테스트 18 〉	통과 (2.68ms, 10.4MB)
테스트 19 〉	통과 (0.56ms, 10.2MB)
테스트 20 〉	통과 (3.82ms, 10.4MB)
테스트 21 〉	통과 (7.93ms, 10.8MB)
테스트 22 〉	통과 (21.88ms, 18MB)
테스트 23 〉	통과 (16.36ms, 11.7MB)
테스트 24 〉	통과 (15.99ms, 11.5MB)
테스트 25 〉	통과 (0.01ms, 10MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10MB)
"""