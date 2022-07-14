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

# 더 좋은 방법
from collections import deque
def solution(priorities, location):
    q = deque()
    for i, priority in enumerate(priorities):
        q.append((i, priority))
    # 현재 큐에서 가장 높은 우선 순위 값
    _max = max([x[1] for x in q])
    
    count = 1
    # while True 도 가능
    while q:
        i, priority = q.popleft()
        if i == location and priority == _max:
            return count
        
        # 꺼낸 문서가 target이 아니고 가장 높은 우선순위라면 출력
        if _max == priority:
            # 남은 문서 중 가장 높은 우선순위를 다시 구하고
            _max = max([x[1] for x in q])
            # 문서를 출력했으므로 +1
            count += 1
        # 그렇지 않다면 다시 프린터에 넣어준다.
        else:
            q.append((i, priority))

"""
정확성  테스트
테스트 1 〉	통과 (0.21ms, 10.2MB)
테스트 2 〉	통과 (0.33ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.09ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.25ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.2MB)
테스트 11 〉	통과 (0.34ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.16ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.39ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.39ms, 10.2MB)
테스트 20 〉	통과 (0.05ms, 10.3MB)
"""
# 바로 위 풀이에서는 max 값을 계속 구하고 있음, max()는 O(N)의 시간복잡도
# 따라서 count를 index로 하여 더 최적화
from collections import deque
def solution(priorities, location):
    q = deque()
    for i, priority in enumerate(priorities):
        q.append((i, priority))
    # 현재 큐에서 가장 높은 우선 순위 값
    count = 0
    rev_priorities = sorted(priorities, reverse = True)
    while q:
        _max = rev_priorities[count]
        i, priority = q.popleft()
        if i == location and priority == _max:
            return count + 1
        # 꺼낸 문서가 target이 아니고 가장 높은 우선순위라면 출력
        if _max == priority:
            # 문서를 출력했으므로 +1, 따라서 우선순위 값도 그 다음 우선순위 값이 될 것임
            count += 1
        # 그렇지 않다면 다시 프린터에 넣어준다.
        else:
            q.append((i, priority))
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (0.12ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.08ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.06ms, 10.3MB)
테스트 20 〉	통과 (0.03ms, 10.3MB)
"""