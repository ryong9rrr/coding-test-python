def get_prev_max(prev_row, currrent_j):
    result = -float('inf')
    for j in range(4):
        if j != currrent_j:
            result = max(result, prev_row[j])
    return result


def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0]
    
    for i in range(1, N):
        for j in range(4):
            dp[i][j] = get_prev_max(dp[i - 1], j) + land[i][j]
    
    return max(dp[-1])
"""
정확성  테스트
테스트 1 〉	통과 (4.90ms, 10.4MB)
테스트 2 〉	통과 (8.59ms, 10.3MB)
테스트 3 〉	통과 (6.88ms, 10.2MB)
테스트 4 〉	통과 (5.12ms, 10.3MB)
테스트 5 〉	통과 (8.46ms, 10.4MB)
테스트 6 〉	통과 (4.50ms, 10.2MB)
테스트 7 〉	통과 (4.50ms, 10.2MB)
테스트 8 〉	통과 (9.17ms, 10.2MB)
테스트 9 〉	통과 (4.33ms, 10.3MB)
테스트 10 〉	통과 (4.32ms, 10.2MB)
테스트 11 〉	통과 (4.40ms, 10.4MB)
테스트 12 〉	통과 (4.37ms, 10.1MB)
테스트 13 〉	통과 (4.41ms, 10.4MB)
테스트 14 〉	통과 (4.36ms, 10.2MB)
테스트 15 〉	통과 (4.71ms, 10.4MB)
테스트 16 〉	통과 (4.38ms, 10.4MB)
테스트 17 〉	통과 (8.53ms, 10.4MB)
테스트 18 〉	통과 (4.65ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (423.90ms, 43.2MB)
테스트 2 〉	통과 (467.56ms, 43.1MB)
테스트 3 〉	통과 (464.55ms, 43.2MB)
테스트 4 〉	통과 (466.29ms, 43.1MB)
"""