def get_prev_max(prev_row, currrent_j):
    return max([v for j, v in enumerate(prev_row) if j != currrent_j ])


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
테스트 1 〉	통과 (4.04ms, 10.1MB)
테스트 2 〉	통과 (6.20ms, 10.2MB)
테스트 3 〉	통과 (6.64ms, 10.2MB)
테스트 4 〉	통과 (3.46ms, 10.2MB)
테스트 5 〉	통과 (6.67ms, 10.2MB)
테스트 6 〉	통과 (3.57ms, 10.2MB)
테스트 7 〉	통과 (3.48ms, 10.2MB)
테스트 8 〉	통과 (3.57ms, 10.2MB)
테스트 9 〉	통과 (6.28ms, 10.2MB)
테스트 10 〉	통과 (3.51ms, 10.2MB)
테스트 11 〉	통과 (6.87ms, 10.1MB)
테스트 12 〉	통과 (6.94ms, 10.1MB)
테스트 13 〉	통과 (3.72ms, 10.2MB)
테스트 14 〉	통과 (6.97ms, 10.3MB)
테스트 15 〉	통과 (3.82ms, 10.1MB)
테스트 16 〉	통과 (6.71ms, 10.3MB)
테스트 17 〉	통과 (6.25ms, 10.4MB)
테스트 18 〉	통과 (6.68ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (377.99ms, 43.3MB)
테스트 2 〉	통과 (378.54ms, 43.2MB)
테스트 3 〉	통과 (381.46ms, 43.3MB)
테스트 4 〉	통과 (381.60ms, 43.2MB)
"""