import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
216ms

상어가 먹을 수 있는 물고기를 모두 다 먹는데 걸리는 시간을 구해라

- [x] 처음 상어의 크기 : 2
- [x] 상어는 자신보다 큰 물고기가 있는 칸은 지나갈 수 없고 나머지는 지나갈 수 있다.

- [x] 상어는 자신보다 작은 물고기만 먹을 수 있다.
- [x] 더 이상 먹을 수 있는 물고기가 없다면 프로그램을 종료한다.
- [x] 거리가 동일한 물고기가 여러마리라면 위 - 왼쪽 순으로 먹는다.
- [x] 먹을 수 있는 물고기가 있다면 그 물고기를 먹으러 간다.(그 물고기의 위치로 이동한다.)
- [x] 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다
"""

INF = int(1e9)

N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

current_shark_size = 2
current_shark_x = current_shark_y = 0
# 처음 상어의 위치를 초기화하고 그 위치를 0으로 바꾼다.
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            current_shark_x = i
            current_shark_y = j
            break

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def validate_range(x, y):
    return 0 <= x < N and 0 <= y < N

#현재 상어가 도달할 수 있는 거리정보를 반환한다. 거리가 -1이라면 도달할 수 없는 좌표다.
def get_distance_map_bfs():
    q = deque([(current_shark_x, current_shark_y)])
    MAP[current_shark_x][current_shark_y] = 0
    distance_map = [[-1] * N for _ in range(N)]
    distance_map[current_shark_x][current_shark_y] = 0

    # 맵 범위를 벗어나지 않고 아직 지나갔던 적이 없는 좌표며, 물고기의 크기가 상어의 크기 이하라면 지나갈 수 있음
    def can_move(next_x, next_y):
        return validate_range(next_x, next_y) and distance_map[next_x][next_y] == -1 and MAP[next_x][next_y] <= current_shark_size

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if can_move(nx, ny):
                # 거리를 +1 한다. 이렇게하면 거리를 기록하면서 이미 지나간 자리라는 정보도 제공해줄 수 있음
                distance_map[nx][ny] = distance_map[x][y] + 1
                q.append((nx, ny))

    return distance_map

def find_can_eat_fish(distance_map):
    # 이렇게 루프를 돌리면 자연스럽게 위 - 왼쪽 순으로 물고기를 찾게 된다.
    distance = INF
    target_fish = None

    for i in range(N):
        for j in range(N):
            # 물고기가 있는 자리고, 크기가 자신보다 작으며, 갈 수 있는 좌표이고, 현재 가장 가까운 거리에 있는 물고기이라면 먹는다.
            if MAP[i][j] != 0 and MAP[i][j] < current_shark_size and distance_map[i][j] != -1 and distance_map[i][j] < distance:
                distance = distance_map[i][j]
                target_fish = (i, j)

    if not target_fish or distance == INF:
        return None
    return target_fish[0], target_fish[1], distance

ate_fish_count = 0
total_distance = 0
#물고기를 찾고 먹기 시작
while True:
    found_result = find_can_eat_fish(get_distance_map_bfs())
    if not found_result:
        break
    x, y, distance = found_result
    # 먹은 물고기 수를 늘리고, 거리를 누적하고, 상어의 위치를 이동시킨다.
    ate_fish_count += 1
    total_distance += distance
    current_shark_x = x
    current_shark_y = y
    # 만약 상어의 크기가 먹은 물고기의 수와 같아지면 상어의 크기를 늘리고, 물고기 수를 초기화한다.
    if current_shark_size == ate_fish_count:
        current_shark_size += 1
        ate_fish_count = 0

print(total_distance)