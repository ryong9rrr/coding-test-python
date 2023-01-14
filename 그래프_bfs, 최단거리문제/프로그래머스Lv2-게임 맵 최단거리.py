from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque()
    q.append((0, 0, 1))
    
    while q:
        x, y, count = q.popleft()
        if x == N - 1 and y == M - 1:
            return count
        
        maps[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = 0 # 여기서 마킹을 해줌으로써 불필요한 연산을 덜어낸다. (최적화)
                q.append((nx, ny, count + 1))
    
    return -1
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.1MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.04ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.4MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (12.08ms, 10.2MB)
테스트 2 〉	통과 (3.28ms, 10.3MB)
테스트 3 〉	통과 (8.45ms, 10.4MB)
테스트 4 〉	통과 (5.42ms, 10.2MB)
"""