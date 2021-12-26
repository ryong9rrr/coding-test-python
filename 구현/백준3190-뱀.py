# 반복문을 이용한 풀이
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
K = int(input())
for _ in range(K):
    n, m = map(int, input().split())
    matrix[n][m] = 1 #사과
L = int(input())
info = []
for _ in range(L):
    X, C = input().split()
    info.append((int(X), C))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction:int, c:str)->int:
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    matrix[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = deque()
    q.append((x, y))

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= N and 1 <= ny and ny <= N and matrix[nx][ny] != 2:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.popleft()
                matrix[px][py] = 0
            elif matrix[nx][ny] == 1:
                matrix[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < L and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())