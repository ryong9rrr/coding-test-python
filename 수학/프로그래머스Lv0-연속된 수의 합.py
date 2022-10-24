def solution(num, total):
    """
    x부터 n개까지의 연속된 정수의 수열의 합이 f일 때,
    f = nx + (1부터 n-1 까지의 합) 이라고 할 수 있다.
    즉, f = nx + (n(n - 1) / 2) 이고
    x = (f - ((n(n - 1) / 2))) / n
    """
    x = (total - ((num * (num - 1) // 2))) // num
    
    result = []
    for _ in range(num):
        result.append(x)
        x += 1
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 9.91MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 9.91MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 9.99MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
"""