from collections import deque
def is_valid(s):
    stack = []
    for char in s:
        if char == "]" or char == ")" or char == "}":
            if not stack:
                return False
            top = stack[-1]
            if (top == "[" and char == "]") or (top == "(" and char == ")") or (top == "{" and char == "}"):
               stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0

def solution(s):
    q = deque(s)

    result = 0
    for i in range(len(s)):
        string = "".join(q)
        if is_valid(string):
            result += 1
        q.append(q.popleft())
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (16.78ms, 10.4MB)
테스트 2 〉	통과 (13.25ms, 10.2MB)
테스트 3 〉	통과 (13.05ms, 10.3MB)
테스트 4 〉	통과 (15.07ms, 10.3MB)
테스트 5 〉	통과 (31.17ms, 10.2MB)
테스트 6 〉	통과 (17.50ms, 10.3MB)
테스트 7 〉	통과 (21.06ms, 10.1MB)
테스트 8 〉	통과 (25.09ms, 10.3MB)
테스트 9 〉	통과 (42.30ms, 10.1MB)
테스트 10 〉	통과 (57.29ms, 10.3MB)
테스트 11 〉	통과 (84.05ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
"""

# leetcode20(Easy) - 유효한 괄호 문제와 거의 동일한 문제
from collections import deque
def is_valid(s):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for bracket in s:
        if bracket not in table:
            stack.append(bracket)
        elif not stack or table[bracket] != stack.pop():
            return False
        
    return len(stack) == 0

def solution(s):
    q = deque(s)

    result = 0
    for i in range(len(s)):
        string = "".join(q)
        if is_valid(string):
            result += 1
        q.append(q.popleft())
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (13.87ms, 10.1MB)
테스트 2 〉	통과 (11.57ms, 10.3MB)
테스트 3 〉	통과 (11.56ms, 10.3MB)
테스트 4 〉	통과 (12.72ms, 10.2MB)
테스트 5 〉	통과 (22.90ms, 10.3MB)
테스트 6 〉	통과 (14.68ms, 10.1MB)
테스트 7 〉	통과 (18.55ms, 10.2MB)
테스트 8 〉	통과 (19.89ms, 10.1MB)
테스트 9 〉	통과 (33.62ms, 10.2MB)
테스트 10 〉	통과 (41.87ms, 10MB)
테스트 11 〉	통과 (62.19ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
"""