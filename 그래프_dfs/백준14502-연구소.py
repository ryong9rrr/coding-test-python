# 32884KB, 5116ms
import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
MATRIX = []
matrix = [[0] * M for _ in range(N)]

for _ in range(N):
    row = list(input().split())
    MATRIX.append(row)

empties = []
for i in range(N):
    for j in range(M):
        if MATRIX[i][j] == "0":
            empties.append([i, j])

combis = list(combinations(empties, 3))

def copy_matrix():
    for i in range(N):
        for j in range(M):
            matrix[i][j] = MATRIX[i][j]

def dfs(i, j):
    # 빈 공간이 아니면 바로 리턴
    if i < 0 or i >= N or j < 0 or j >= M or matrix[i][j] != "0":
        return
    matrix[i][j] = "2"
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
    return

def search_empties():
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "0":
                count += 1
    return count

result = 0

for combi in combis:
    # 벽을 세워봄
    for i, j in combi:
        MATRIX[i][j] = "1"
    copy_matrix()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "2":
                # dfs를 위해 임시로 빈공간으로 만들어줌
                matrix[i][j] = "0"
                dfs(i, j)
    count = search_empties()
    result = max(result, count)
    # 다시 벽 제거
    for i, j in combi:
        MATRIX[i][j] = "0"

print(result)


# 이코테 풀이는 시간초과가 나온다. (오히려 좋아..)
"""
n, m = map(int, input().split())
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트
graph = [list(map(int, input().split())) for _ in range(n)] # 초기 맵 리스트

result = 0

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 깊이 우선 탐색을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상,하,좌,우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스를 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)
"""