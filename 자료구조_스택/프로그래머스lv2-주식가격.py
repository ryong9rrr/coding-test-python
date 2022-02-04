def solution(prices):
    
    stack = []
    result = []
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            prev_i = stack.pop()
            result.append((prev_i, i - prev_i))
        stack.append(i)
    
    for index in stack:
        result.append((index, len(prices) - index - 1))
    
    return [x[1] for x in sorted(result, key = lambda x: x[0])]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.40ms, 10.3MB)
테스트 4 〉	통과 (0.79ms, 10.4MB)
테스트 5 〉	통과 (0.56ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.48ms, 10.3MB)
테스트 8 〉	통과 (0.34ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.58ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (54.24ms, 24.8MB)
테스트 2 〉	통과 (34.02ms, 21MB)
테스트 3 〉	통과 (56.82ms, 26.2MB)
테스트 4 〉	통과 (43.18ms, 22.5MB)
테스트 5 〉	통과 (30.02ms, 19.3MB)
"""