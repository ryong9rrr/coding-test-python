from collections import deque
def solution(priorities, location):
    q = deque()
    for v in priorities:
        q.append(v)
    
    result = 1
    while q:
        x = q.popleft()
        if not q:
            return result
        
        _max = max(q)
        if x < _max:
            q.append(x)
        else:
            if location == 0:
                return result
            else:
                result += 1
        
        if location == 0:
            location = len(q) - 1
        else:
            location -= 1

"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.59ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.40ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.08ms, 10.2MB)
테스트 11 〉	통과 (0.32ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.27ms, 10.4MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.96ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.39ms, 10.2MB)
테스트 20 〉	통과 (0.06ms, 10.4MB)
"""