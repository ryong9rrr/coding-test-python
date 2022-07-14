from collections import deque
def solution(s):
    stack = deque()
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (6.72ms, 10.3MB)
테스트 3 〉	통과 (8.64ms, 10.5MB)
테스트 4 〉	통과 (8.43ms, 10.6MB)
테스트 5 〉	통과 (8.44ms, 10.5MB)
테스트 6 〉	통과 (8.44ms, 10.6MB)
테스트 7 〉	통과 (8.96ms, 10.7MB)
테스트 8 〉	통과 (8.55ms, 10.4MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (88.33ms, 14.9MB)
테스트 2 〉	통과 (65.79ms, 11.9MB)
테스트 3 〉	통과 (82.17ms, 12.5MB)
테스트 4 〉	통과 (88.59ms, 12.5MB)
테스트 5 〉	통과 (91.05ms, 12.4MB)
테스트 6 〉	통과 (80.40ms, 12.6MB)
테스트 7 〉	통과 (89.04ms, 12.6MB)
테스트 8 〉	통과 (89.39ms, 13.3MB)
"""