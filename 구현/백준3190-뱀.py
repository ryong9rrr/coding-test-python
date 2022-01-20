# while 반복문을 이용한 풀이
from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
# n x n 행렬 (사과가 있는 곳은 1)
matrix = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    matrix[x][y] = 1
l = int(input())
# 방향 회전 정보
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

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
        nx, ny = x + dx[direction], y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and matrix[nx][ny] != 2:
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
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())


################# 코드를 조금 짧게
from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
# n x n 행렬 (사과가 있는 곳은 1)
matrix = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    matrix[x][y] = 1
l = int(input())
# 방향 회전 정보
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

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
    direction = time = index = 0
    q = deque()
    q.append((x, y))
    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and matrix[nx][ny] != 2:
            if matrix[nx][ny] == 0:
                px, py = q.popleft()
                matrix[px][py] = 0
                q.append((nx, ny))
            elif matrix[nx][ny] == 1:
                q.append((nx, ny))
            matrix[nx][ny] = 2
        else:
            time += 1
            return time
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
        x, y = nx, ny

print(simulate())