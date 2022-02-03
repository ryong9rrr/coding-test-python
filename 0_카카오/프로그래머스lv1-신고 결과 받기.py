from collections import defaultdict
def solution(id_list, report, k):
    banned = defaultdict(int)
    info = defaultdict(set)
    
    for i in range(len(report)):
        f_user, t_user = report[i].split(" ")
        info[f_user].add(t_user)
    
    for v in info.values():
        for user in v:
            banned[user] += 1
    
    result = []
    for user in id_list:
        count = 0
        for banned_user in info[user]:
            if banned[banned_user] >= k:
                count += 1
        result.append(count)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (138.93ms, 44.3MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.99ms, 10.6MB)
테스트 7 〉	통과 (2.07ms, 10.6MB)
테스트 8 〉	통과 (3.53ms, 10.8MB)
테스트 9 〉	통과 (63.53ms, 26.6MB)
테스트 10 〉	통과 (60.71ms, 26.4MB)
테스트 11 〉	통과 (178.90ms, 44.3MB)
테스트 12 〉	통과 (0.26ms, 10.3MB)
테스트 13 〉	통과 (0.25ms, 10.4MB)
테스트 14 〉	통과 (65.44ms, 23.5MB)
테스트 15 〉	통과 (120.50ms, 38.7MB)
테스트 16 〉	통과 (0.16ms, 10.2MB)
테스트 17 〉	통과 (0.25ms, 10.4MB)
테스트 18 〉	통과 (0.44ms, 10.4MB)
테스트 19 〉	통과 (1.10ms, 10.4MB)
테스트 20 〉	통과 (58.20ms, 23.6MB)
테스트 21 〉	통과 (137.45ms, 38.6MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
"""