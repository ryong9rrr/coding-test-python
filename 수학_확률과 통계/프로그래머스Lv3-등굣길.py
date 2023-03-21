# 확률과 통계 - 최단거리 경우의 수 문제 ) 동적계획법 방식으로 풀이한다.
# 참고한 블로그 : https://m.blog.naver.com/parkhc1992/220669287080
def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 0
        
    for j in range(m + 1):
        dp[0][j] = 0
    
    for j, i in puddles:
        dp[i][j] = 0
    
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] != -1:
                continue
            dp[i][j] = (dp[i - 1][j] % MOD + dp[i][j - 1] % MOD) % MOD
            
    return dp[n][m]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.10ms, 10.1MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (0.14ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (2.61ms, 10.1MB)
테스트 2 〉	통과 (1.07ms, 10.2MB)
테스트 3 〉	통과 (1.08ms, 10.3MB)
테스트 4 〉	통과 (2.17ms, 10.4MB)
테스트 5 〉	통과 (1.42ms, 10.3MB)
테스트 6 〉	통과 (2.84ms, 10.2MB)
테스트 7 〉	통과 (1.18ms, 10.1MB)
테스트 8 〉	통과 (1.82ms, 10.2MB)
테스트 9 〉	통과 (1.98ms, 10.4MB)
테스트 10 〉	통과 (2.00ms, 10.1MB)
"""