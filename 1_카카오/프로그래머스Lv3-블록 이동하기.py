from collections import deque
def get_next_paths(robot, matrix):
    # 위, 아래, 왼쪽, 오른쪽
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    paths = []
    robot = list(robot)
    x1, y1, x2, y2 = robot[0][0], robot[0][1], robot[1][0], robot[1][1]
    # 1. 이동시킬 수 있는지 확인
    for d in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[d], y1 + dy[d], x2 + dx[d], y2 + dy[d]
        if matrix[nx1][ny1] == 0 and matrix[nx2][ny2] == 0:
            paths.append({(nx1, ny1), (nx2, ny2)})
    # 2. 회전시킬 수 있는지 확인
    # 2-1. 가로로 놓여있다면 위, 아래로 회전시킬 수 있는지
    if x1 == x2:
        if matrix[x1 - 1][y1] == 0 and matrix[x2 - 1][y2] == 0:
            paths.append({(x1, y1), (x1 - 1, y1)})
            paths.append({(x2, y2), (x2 - 1, y2)})
        if matrix[x1 + 1][y1] == 0 and matrix[x2 + 1][y2] == 0:
            paths.append({(x1, y1), (x1 + 1, y1)})
            paths.append({(x2, y2), (x2 + 1, y2)})
    # 2-2. 세로로 놓여있다면 왼쪽, 오른쪽으로 회전
    if y1 == y2:
        if matrix[x1][y1 - 1] == 0 and matrix[x2][y2 - 1] == 0:
            paths.append({(x1, y1), (x1, y1 - 1)})
            paths.append({(x2, y2), (x2, y2 - 1)})
        if matrix[x1][y1 + 1] == 0 and matrix[x2][y2 + 1] == 0:
            paths.append({(x1, y1), (x1, y1 + 1)})
            paths.append({(x2, y2), (x2, y2 + 1)})
    return paths

def solution(board):
    N = len(board)
    matrix = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            matrix[i + 1][j + 1] = board[i][j]
    
    visited = []
    q = deque()
    robot = {(1, 1), (1, 2)} # set([(1, 1), (1, 2)]) 과 같음
    q.append((robot, 0))
    visited.append(robot)
    
    while q:
        robot, cost = q.popleft()
        if (N, N) in robot:
            return cost
        for path in get_next_paths(robot, matrix):
            if path not in visited:
                q.append((path, cost + 1))
                visited.append(path)
    
    return 0
"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.4MB)
테스트 2 〉	통과 (0.19ms, 10.2MB)
테스트 3 〉	통과 (0.17ms, 10.3MB)
테스트 4 〉	통과 (1.08ms, 10.3MB)
테스트 5 〉	통과 (0.53ms, 10.3MB)
테스트 6 〉	통과 (1.57ms, 10.2MB)
테스트 7 〉	통과 (8.18ms, 10.3MB)
테스트 8 〉	통과 (9.79ms, 10.3MB)
테스트 9 〉	통과 (13.87ms, 10.1MB)
테스트 10 〉	통과 (6.97ms, 10.3MB)
테스트 11 〉	통과 (4.76ms, 10.3MB)
테스트 12 〉	통과 (6.72ms, 10.2MB)
테스트 13 〉	통과 (2318.97ms, 12.6MB)
테스트 14 〉	통과 (1196.16ms, 11.8MB)
"""