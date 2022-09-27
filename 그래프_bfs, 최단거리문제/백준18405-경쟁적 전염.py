# 33000KB	172ms
# BFS라기보다는 2차원 배열 + Queue 문제
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
matrix = []
temp = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
S, X, Y = map(int, input().split())

viruses = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            viruses.append((matrix[i][j], (i, j)))
viruses.sort(key=lambda x:x[0])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def multiply(score, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = score
                temp.append((score, (nx, ny)))

q = deque(viruses)
while S:
    temp = []
    while q:
        item = q.popleft()
        score = item[0]
        x, y = item[1]
        multiply(score, x, y)
    if temp:
        for item in temp:
            q.append(item)
    S -= 1

print(matrix[X - 1][Y - 1])