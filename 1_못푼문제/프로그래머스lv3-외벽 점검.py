# 이코테
from itertools import permutations
def solution(n, weak, dist):
    friends_permutations = list(permutations(dist, len(dist)))
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(length):
        for friends in friends_permutations:
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.11ms, 10MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (1253.21ms, 14.8MB)
테스트 4 〉	통과 (1158.68ms, 14.9MB)
테스트 5 〉	통과 (2.71ms, 10.2MB)
테스트 6 〉	통과 (193.49ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.52ms, 10MB)
테스트 9 〉	통과 (0.50ms, 10.1MB)
테스트 10 〉	통과 (1905.92ms, 14.8MB)
테스트 11 〉	통과 (1760.09ms, 14.8MB)
테스트 12 〉	통과 (1860.94ms, 14.8MB)
테스트 13 〉	통과 (1820.60ms, 14.8MB)
테스트 14 〉	통과 (1768.41ms, 14.9MB)
테스트 15 〉	통과 (1902.52ms, 14.8MB)
테스트 16 〉	통과 (1372.74ms, 14.9MB)
테스트 17 〉	통과 (1518.77ms, 14.8MB)
테스트 18 〉	통과 (1410.85ms, 14.8MB)
테스트 19 〉	통과 (1103.18ms, 14.9MB)
테스트 20 〉	통과 (1287.90ms, 14.8MB)
테스트 21 〉	통과 (1383.10ms, 14.6MB)
테스트 22 〉	통과 (0.28ms, 10.2MB)
테스트 23 〉	통과 (0.49ms, 10.2MB)
테스트 24 〉	통과 (0.56ms, 10.2MB)
테스트 25 〉	통과 (537.49ms, 14.8MB)
"""

# 베스트풀이
from collections import deque

def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                if l < r:
                    temp = tuple(filter(lambda x: x < l or x > r, current))
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current))

                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
    return -1
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (22.61ms, 11MB)
테스트 4 〉	통과 (5.70ms, 10.3MB)
테스트 5 〉	통과 (1.57ms, 10.2MB)
테스트 6 〉	통과 (15.50ms, 10.8MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.10ms, 10.1MB)
테스트 9 〉	통과 (0.19ms, 10.2MB)
테스트 10 〉	통과 (69.70ms, 12.4MB)
테스트 11 〉	통과 (46.48ms, 11.6MB)
테스트 12 〉	통과 (47.10ms, 11.6MB)
테스트 13 〉	통과 (321.56ms, 16.4MB)
테스트 14 〉	통과 (139.00ms, 12.9MB)
테스트 15 〉	통과 (34.17ms, 11.4MB)
테스트 16 〉	통과 (0.62ms, 10.3MB)
테스트 17 〉	통과 (6.83ms, 10.5MB)
테스트 18 〉	통과 (2.27ms, 10.3MB)
테스트 19 〉	통과 (0.12ms, 10.2MB)
테스트 20 〉	통과 (0.90ms, 10.1MB)
테스트 21 〉	통과 (0.12ms, 10.1MB)
테스트 22 〉	통과 (1.45ms, 10.1MB)
테스트 23 〉	통과 (3.13ms, 10.2MB)
테스트 24 〉	통과 (2.40ms, 10.3MB)
테스트 25 〉	통과 (0.35ms, 10.2MB)
"""
