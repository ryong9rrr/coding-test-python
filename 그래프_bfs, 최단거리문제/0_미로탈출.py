"""
bfs 문제

5 x 6 형태의 미로에서 (0,0)에서 (5,6)까지의 최단거리를 구해라

1. 1은 길이고 0은 길이 아님.

101010
111111
000001
111111
111111

-> 10
"""

from collections import deque

_map = [
    "101010",
    "111111",
    "000001",
    "111111",
    "111111"
]
n, m = 5, 6
graph = [list(x) for x in _map]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# (y, x)는 시작지점, 가장 오른쪽 아래까지 최단거리를 반환하는 함수
def bfs(y:int, x:int)->int:
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        # 4방향 확인
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if nx < 0 or ny < 0 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] == "0":
                continue
            if graph[ny][nx] == "1":
                graph[ny][nx] = str(int(graph[y][x]) + 1)
                q.append((ny, nx))
    return graph[n-1][m-1]

print(bfs(0, 0)) # 10