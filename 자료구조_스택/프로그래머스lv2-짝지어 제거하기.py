from collections import deque
def solution(s):
    stack = deque()
    for a in s:
        # stack 맨위의 문자와 지금 넣는 문자가 같으면 stack에서 빼버림.
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)
    
    return 0 if stack else 1

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (6.83ms, 10.3MB)
테스트 3 〉	통과 (12.08ms, 10.5MB)
테스트 4 〉	통과 (12.00ms, 10.7MB)
테스트 5 〉	통과 (8.71ms, 10.5MB)
테스트 6 〉	통과 (13.75ms, 10.6MB)
테스트 7 〉	통과 (8.51ms, 10.6MB)
테스트 8 〉	통과 (17.39ms, 10.5MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (88.20ms, 14.8MB)
테스트 2 〉	통과 (67.57ms, 11.8MB)
테스트 3 〉	통과 (88.66ms, 12.5MB)
테스트 4 〉	통과 (88.34ms, 12.5MB)
테스트 5 〉	통과 (88.55ms, 12.6MB)
테스트 6 〉	통과 (88.43ms, 12.6MB)
테스트 7 〉	통과 (80.10ms, 12.6MB)
테스트 8 〉	통과 (80.87ms, 13.3MB)
"""