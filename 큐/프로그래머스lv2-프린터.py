from collections import deque

def solution(priorities, location):
    q = deque([(i, x) for i, x in enumerate(priorities)])
    maxes = sorted(priorities)
    
    count = 0
    while q:
        loc, p = q.popleft()
        if p == maxes[-1]:
            if loc == location:
                return count + 1
            count += 1
            maxes.pop()
        q.append((loc, p))
"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.14ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.06ms, 10.3MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.15ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.13ms, 10.4MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.15ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10MB)
테스트 19 〉	통과 (0.12ms, 10.2MB)
테스트 20 〉	통과 (0.04ms, 10.3MB)
"""