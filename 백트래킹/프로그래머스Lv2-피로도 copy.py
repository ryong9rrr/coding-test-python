# 순열
from itertools import permutations

def solution(k, dungeons):
    result = 0
    for dg in list(permutations(dungeons, len(dungeons))):
        count = 0
        dungeon = list(dg)
        my_p = k
        while dungeon and my_p > 0:
            min_p, p = dungeon.pop()
            if min_p > my_p:
                continue
            count += 1
            my_p -= p
        result = max(result, count)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.19ms, 10.3MB)
테스트 4 〉	통과 (0.23ms, 10.2MB)
테스트 5 〉	통과 (1.57ms, 10.3MB)
테스트 6 〉	통과 (11.77ms, 10.3MB)
테스트 7 〉	통과 (57.35ms, 14.8MB)
테스트 8 〉	통과 (60.40ms, 14.6MB)
테스트 9 〉	통과 (0.21ms, 10.3MB)
테스트 10 〉	통과 (6.91ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (54.56ms, 14.8MB)
테스트 13 〉	통과 (54.69ms, 14.8MB)
테스트 14 〉	통과 (55.58ms, 14.9MB)
테스트 15 〉	통과 (62.07ms, 14.8MB)
테스트 16 〉	통과 (5.55ms, 10.4MB)
테스트 17 〉	통과 (58.88ms, 14.8MB)
테스트 18 〉	통과 (0.04ms, 10.2MB)
테스트 19 〉	통과 (0.12ms, 10.1MB)
"""

# 백트래킹
def solution(k, dungeons):
    global result
    N = len(dungeons)
    visited = [0] * N
    result = 0
    
    def dfs(my_p, count):
        global result
        result = max(result, count)
        
        for i in range(N):
            min_p, p = dungeons[i]
            if my_p >= min_p and not visited[i]:
                visited[i] = 1
                dfs(my_p - p, count + 1)
                visited[i] = 0
                
    dfs(k, 0)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.47ms, 10.2MB)
테스트 5 〉	통과 (1.60ms, 10.2MB)
테스트 6 〉	통과 (5.44ms, 10MB)
테스트 7 〉	통과 (26.88ms, 10.1MB)
테스트 8 〉	통과 (63.59ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (0.97ms, 10MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (2.77ms, 10.2MB)
테스트 13 〉	통과 (0.30ms, 10.1MB)
테스트 14 〉	통과 (0.61ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (0.07ms, 10.3MB)
테스트 17 〉	통과 (0.17ms, 10.2MB)
테스트 18 〉	통과 (0.04ms, 10.1MB)
테스트 19 〉	통과 (0.12ms, 10.1MB)
"""