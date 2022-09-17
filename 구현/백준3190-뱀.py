import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 입력받기
N = int(input())
K = int(input())
# 편의상 N + 1로 해서 (N + 1) x (N + 1) 행렬 생성
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    # 사과가 있는 곳은 1로 표시
    matrix[r][c] = 1
L = int(input())
# 앞에서 부터 하나하나 뺄 것이므로, x가 증가하는대로 주어지므로 정렬은 할 필요 없다.
infos = deque()
for _ in range(L):
    x, c = input().split()
    infos.append((int(x), c))

# for row in matrix:
#     print(row)

# 처음에는 동쪽(오른쪽)으로 이동하므로 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        return (direction - 1) % 4
    return (direction + 1) % 4

cur_x = cur_y = 1
matrix[cur_x][cur_y] = 2
direction = time = 0
snakes = deque()
snakes.append([cur_x, cur_y])

while True:
    next_x = cur_x + dx[direction]
    next_y = cur_y + dy[direction]
    if 1 <= next_x and next_x <= N and 1 <= next_y and next_y <= N and matrix[next_x][next_y] != 2:
        if matrix[next_x][next_y] == 0:
            prev_x, prev_y = snakes.popleft()
            matrix[prev_x][prev_y] = 0
        matrix[next_x][next_y] = 2
        snakes.append([next_x, next_y])
    else:
        break
    time += 1
    cur_x, cur_y = next_x, next_y
    if infos and time == infos[0][0]:
        direction = turn(direction, infos[0][1])
        infos.popleft()

print(time + 1)