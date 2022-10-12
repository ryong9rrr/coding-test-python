# 백준 1932번과 동일한 문제
def search_prev_max_value(i, j, DP):
    max_value = 0
    for d in [-1, 0]:
        pj = j + d
        if 0 <= pj < i:
            max_value = max(max_value, DP[i - 1][pj])
    return max_value

def solution(triangle):
    N = len(triangle)
    for i in range(1, N):
        for j in range(i + 1):
            triangle[i][j] += search_prev_max_value(i, j, triangle)
    
    return max(triangle[-1])
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.1MB)
테스트 4 〉	통과 (0.30ms, 10.2MB)
테스트 5 〉	통과 (2.07ms, 10.3MB)
테스트 6 〉	통과 (0.61ms, 10.2MB)
테스트 7 〉	통과 (2.11ms, 10.1MB)
테스트 8 〉	통과 (0.48ms, 10MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.29ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (65.24ms, 14.1MB)
테스트 2 〉	통과 (50.99ms, 13.2MB)
테스트 3 〉	통과 (70.49ms, 14.7MB)
테스트 4 〉	통과 (61.73ms, 14.1MB)
테스트 5 〉	통과 (57.22ms, 14MB)
테스트 6 〉	통과 (76.14ms, 14.6MB)
테스트 7 〉	통과 (71.25ms, 14.4MB)
테스트 8 〉	통과 (54.81ms, 13.7MB)
테스트 9 〉	통과 (58.00ms, 13.9MB)
테스트 10 〉	통과 (72.87ms, 14.4MB)
"""