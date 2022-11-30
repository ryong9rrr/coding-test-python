# 제일 처음에 푼 큐와 임시 스택 풀이...
from collections import deque
def solution(ingredient):
    # 빵(1) - 야채(2) - 고기(3) - 빵(1) 순서로
    q = deque(ingredient)
    stack = []

    result = 0

    while q:
        x = q.popleft()
        if x == 1 and len(q) > 2 and q[0] == 2 and q[1] == 3 and q[2] == 1:
            n = 3
            while n:
                q.popleft()
                n -= 1
            result += 1
            while stack and q:
                if not stack[-1] == 1 and q[0] == 2:
                    break
                if not stack[-1] == 2 and q[0] == 3:
                    break
                if not stack[-1] == 3 and q[0] == 1:
                    break
                q.appendleft(stack.pop())
        else:
            stack.append(x)

    return result

"""
정확성 테스트
테스트 1 〉 통과 (0.01ms, 10MB)
테스트 2 〉 통과 (0.01ms, 10.3MB)
테스트 3 〉 통과 (63.28ms, 17.2MB)
테스트 4 〉 통과 (90.90ms, 25.7MB)
테스트 5 〉 통과 (116.70ms, 29.2MB)
테스트 6 〉 통과 (74.38ms, 21MB)
테스트 7 〉 통과 (87.35ms, 24.4MB)
테스트 8 〉 통과 (68.99ms, 21.7MB)
테스트 9 〉 통과 (53.40ms, 18.6MB)
테스트 10 〉 통과 (1.18ms, 10.2MB)
테스트 11 〉 통과 (37.69ms, 16.3MB)
테스트 12 〉 통과 (165.07ms, 33.9MB)
테스트 13 〉 통과 (0.00ms, 10.2MB)
테스트 14 〉 통과 (0.01ms, 10.2MB)
테스트 15 〉 통과 (0.00ms, 10MB)
테스트 16 〉 통과 (0.00ms, 10.2MB)
테스트 17 〉 통과 (0.00ms, 10.3MB)
"""

# 하지만 그냥 스택으로만 풀 수도 있다.
def solution(ingredient):
    stack = []
    result = 0
    
    for x in ingredient:
        stack.append(x)
        if stack[-4:] == [1, 2, 3, 1]:
            result += 1
            for _ in range(4):
                stack.pop()
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (53.49ms, 14.7MB)
테스트 4 〉	통과 (113.70ms, 20.5MB)
테스트 5 〉	통과 (145.86ms, 23.1MB)
테스트 6 〉	통과 (81.75ms, 17.5MB)
테스트 7 〉	통과 (103.24ms, 19.4MB)
테스트 8 〉	통과 (84.14ms, 17.8MB)
테스트 9 〉	통과 (65.58ms, 15.6MB)
테스트 10 〉	통과 (1.48ms, 10.2MB)
테스트 11 〉	통과 (45.33ms, 14.3MB)
테스트 12 〉	통과 (176.80ms, 26.6MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
"""