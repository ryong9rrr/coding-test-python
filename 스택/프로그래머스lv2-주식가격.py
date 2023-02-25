# 리트코드 일일온도와 거의 비슷한 문제
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, cur in enumerate(prices):
        while stack and prices[stack[-1]] > cur:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
        
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top
    
    return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.40ms, 10.2MB)
테스트 4 〉	통과 (0.22ms, 10.1MB)
테스트 5 〉	통과 (0.26ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.14ms, 10.1MB)
테스트 8 〉	통과 (0.26ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.26ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (22.50ms, 18.8MB)
테스트 2 〉	통과 (16.62ms, 17.5MB)
테스트 3 〉	통과 (27.06ms, 19.4MB)
테스트 4 〉	통과 (18.96ms, 18.2MB)
테스트 5 〉	통과 (14.62ms, 16.9MB)
"""