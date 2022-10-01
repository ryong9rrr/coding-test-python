# 첫번째 풀이 - 80%에서 시간초과
# 평균을 구하는 부분을 따로 카운트해서 최적화했지만 여전히 80%에서 시간초과
# 그래서 그냥 첫번째 풀이를 PyPy3로 제출했다.
# PyPy3 141576KB	1836ms
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, L, R = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def union(i, j, visited, loop_count):
    unions = []
    q = deque()
    q.append((i, j))
    unions.append((i, j))
    visited[i][j] = loop_count
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if L <= abs(matrix[x][y] - matrix[nx][ny]) <= R:
                    unions.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = loop_count
    if unions:
        avg = sum([matrix[x][y] for x, y in unions]) // len(unions)
        for x, y in unions:
            matrix[x][y] = avg
    return

day = 0
while True:
    # 숫자로 마킹을 할 것이므로 초기값은 -1
    visited = [[-1] * N for _ in range(N)]
    # 무한루프를 탈출하기 위한 변수, 이걸로 visited에 마킹을 할 것이다.
    loop_count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                union(i, j, visited, loop_count)
                loop_count += 1
    # 모든 지역을 방문했다면 연합을 만들 수 있는 국가가 없다는 것이므로
    if loop_count == N * N:
        break
    day += 1

print(day)