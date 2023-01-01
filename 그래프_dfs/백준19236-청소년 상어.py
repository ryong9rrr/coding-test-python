# 60ms

import sys
import copy
input = lambda: sys.stdin.readline().rstrip()

MATRIX_RANGE = 4
DIRECTION = 8
DX = [-1, -1, 0, 1, 1, 1, 0, -1]
DY = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0


def turn_left(current_direction, direction_index):
    return (current_direction + direction_index) % DIRECTION


def validate_range(x, y):
    return 0 <= x < MATRIX_RANGE and 0 <= y < MATRIX_RANGE


def create_fish_matrix(f_input):
    fish_matrix = []
    for _ in range(MATRIX_RANGE):
        row = []
        data = list(map(int, f_input().split()))
        for i in range(0, 8, 2):
            number, direction = data[i], data[i + 1]
            row.append((number, direction - 1))
        fish_matrix.append(row)
    return fish_matrix


def find_fish(fish_number, fish_matrix):
    for i in range(MATRIX_RANGE):
        for j in range(MATRIX_RANGE):
            if fish_matrix[i][j] and fish_matrix[i][j][0] == fish_number:
                return i, j
    return None


def swap_fish(fish_x, fish_y, shark_x, shark_y, fish_matrix):
    direction = fish_matrix[fish_x][fish_y][1]
    for i in range(DIRECTION):
        next_direction = turn_left(direction, i)
        next_fish_x = fish_x + DX[next_direction]
        next_fish_y = fish_y + DY[next_direction]
        is_shark = shark_x == next_fish_x and shark_y == next_fish_y
        if validate_range(next_fish_x, next_fish_y) and not is_shark:
            current_fish = (fish_matrix[fish_x][fish_y][0], next_direction)
            fish_matrix[next_fish_x][next_fish_y], fish_matrix[fish_x][fish_y] = current_fish, fish_matrix[next_fish_x][next_fish_y]
            return


def move_fishes(shark_x, shark_y, fish_matrix):
    for fish_number in range(1, MATRIX_RANGE ** 2 + 1):
        found_fish = find_fish(fish_number, fish_matrix)
        if not found_fish:
            continue
        x, y = found_fish
        swap_fish(x, y, shark_x, shark_y, fish_matrix)


def search_eatable_fishes(shark_x, shark_y, shark_direction, fish_matrix):
    positions = []
    for i in range(MATRIX_RANGE):
        shark_x += DX[shark_direction]
        shark_y += DY[shark_direction]
        if validate_range(shark_x, shark_y) and fish_matrix[shark_x][shark_y]:
            positions.append((shark_x, shark_y))
    return positions


def dfs(shark_x, shark_y, fish_matrix, total):
    global result
    matrix = copy.deepcopy(fish_matrix)  # 참조를 막기 위해 리스트 깊은 복사
    if not matrix[shark_x][shark_y]:
        return
    fish_number, fish_direction = matrix[shark_x][shark_y]
    total += fish_number
    matrix[shark_x][shark_y] = None
    # 전체 물고기 이동
    move_fishes(shark_x, shark_y, matrix)
    # 상어 이동
    positions = search_eatable_fishes(shark_x, shark_y, fish_direction, matrix)
    if not positions:
        result = max(result, total)
        return
    for nx, ny in positions:
        dfs(nx, ny, matrix, total)


def solution(f_input):
    fish_matrix = create_fish_matrix(f_input)
    shark_x = shark_y = 0
    total = 0
    dfs(shark_x, shark_y, fish_matrix, total)


solution(input)
print(result)