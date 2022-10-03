from collections import deque
def get_next_paths(robot, matrix):
    paths = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    robot = list(robot) # set자료형을 리스트 자료형으로 변환
    x1, y1, x2, y2 = robot[0][0], robot[0][1], robot[1][0], robot[1][1]
    # 1. 이동시킬 수 있는지 확인
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
        if matrix[nx1][ny1] == 0 and matrix[nx2][ny2] == 0:
            paths.append({(nx1, ny1), (nx2, ny2)})
    # 2. 회전시킬 수 있는지 확인
    # 2-1. 가로로 놓여있다면 위, 아래로 회전시킬 수 있는지
    if x1 == x2:
        for i in [-1, 1]:
            if matrix[x1 + i][y1] == 0 and matrix[x2 + i][y2] == 0:
                paths.append({(x1, y1), (x1 + i, y1)})
                paths.append({(x2, y2), (x2 + i, y2)})
    """
    아래와 같음.
    if x1 == x2:
        if matrix[x1 - 1][y1] == 0 and matrix[x2 - 1][y2] == 0:
            paths.append({(x1, y1), (x1 - 1, y1)})
            paths.append({(x2, y2), (x2 - 1, y2)})
        if matrix[x1 + 1][y1] == 0 and matrix[x2 + 1][y2] == 0:
            paths.append({(x1, y1), (x1 + 1, y1)})
            paths.append({(x2, y2), (x2 + 1, y2)})
    """
    # 2-2. 세로로 놓여있다면 왼쪽, 오른쪽으로 회전
    if y1 == y2:
        for i in [-1, 1]:
            if matrix[x1][y1 + i] == 0 and matrix[x2][y2 + i] == 0:
                paths.append({(x1, y1), (x1, y1 + i)})
                paths.append({(x2, y2), (x2, y2 + i)})
    """
    아래와 같음.
    if y1 == y2:
        if matrix[x1][y1 - 1] == 0 and matrix[x2][y2 - 1] == 0:
            paths.append({(x1, y1), (x1, y1 - 1)})
            paths.append({(x2, y2), (x2, y2 - 1)})
        if matrix[x1][y1 + 1] == 0 and matrix[x2][y2 + 1] == 0:
            paths.append({(x1, y1), (x1, y1 + 1)})
            paths.append({(x2, y2), (x2, y2 + 1)})
    """
    return paths

def solution(board):
    """
    1. 로봇의 현재 위치에서 이동, 회전할 수 있는 방법에 따라서 BFS탐색을 한다.
    2. 로봇의 현재 위치가 (N, N)라면 탐색을 종료한다.
    
    <로봇을 이동시킬 수 있는 경우>
    로봇의 현재 위치가 (x1, y1), (x2, y2)라 할 때, 그냥 이동시킨 곳이 빈칸(0)일 경우 이동이 가능.
    
    <로봇을 회전시킬 수 있는 경우>
    로봇의 현재 위치가 (x1, y1), (x2, y2)라 할 때,
    1. 로봇이 가로방향(x1 == x2)이라면 위, 아래 이동할 수 있는 곳이 모두 빈칸(0)이어야 함.
    2. 로봇이 세로방향(y1 == y2)이라면 왼쪽, 오른쪽 이동할 수 있는 곳이 모두 빈칸(0)이어야 함.
    """
    
    N = len(board)
    matrix = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            matrix[i + 1][j + 1] = board[i][j]

    q = deque()
    robot = {(1, 1), (1, 2)} # set([(1, 1), (1, 2)]) 과 같음
    q.append((robot, 0))
    visited = [robot]
    
    while q:
        robot, time = q.popleft()
        if (N, N) in robot:
            return time
        for path in get_next_paths(robot, matrix):
            if path not in visited:
                q.append((path, time + 1))
                visited.append(path)
    
    return -1
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