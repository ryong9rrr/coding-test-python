# 큐와 스택으로 구현
from collections import deque
def solution(number, k):
    q = deque()
    stack = deque()
    
    for n in number:
        q.append(n)
    
    while q and k:
        while stack and stack[-1] < q[0]:
            stack.pop()
            k -= 1
            if not k:
                break
        stack.append(q.popleft())
        
    while k and stack:
        stack.pop()
        k -= 1
    
    return "".join(stack + q)

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.17ms, 10.2MB)
테스트 5 〉	통과 (0.19ms, 10.3MB)
테스트 6 〉	통과 (3.59ms, 10.3MB)
테스트 7 〉	통과 (7.70ms, 10.9MB)
테스트 8 〉	통과 (18.69ms, 11.6MB)
테스트 9 〉	통과 (22.49ms, 17.9MB)
테스트 10 〉	통과 (128.77ms, 16.8MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
"""