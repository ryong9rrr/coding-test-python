# 이코테 풀이(dfs라기 보다는 2차원 행렬 + 조합 문제)
# python3 30840KB	88ms
import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

"""
1. matrix의 빈칸들 중 3곳을 선택해서 벽을 둔다. (조합)
2. 선생님들의 위치를 딴다.
3. 조합에 따라서 일단 벽을 세워보고
4. 선생님들을 동서남북 방향으로 계속 보낸다.
    - 학생들을 만났다면 return True, 만나지 않았다면 return False.
    - 한번도 학생들을 만나지 않은 조합이 있다면 바로 return.
5. 만약 모든 조합을 확인했는데도 S를 만나지 않은 조합이 없다면 print("NO")
"""

N = int(input())
matrix = []
empties = []
teachers = []
for i in range(N):
    row = input().split()
    for j in range(N):
        if row[j] == "X":
            empties.append((i, j))
        elif row[j] == "T":
            teachers.append((i, j))
    matrix.append(row)

empties_combinations = list(combinations(empties, 3))

def search_left(i, j):
    while j >= 0:
        if matrix[i][j] == "S":
            return True
        if matrix[i][j] == "O":
            return False
        j -= 1
    return False

def search_right(i, j):
    while j < N:
        if matrix[i][j] == "S":
            return True
        if matrix[i][j] == "O":
            return False
        j += 1
    return False

def search_top(i, j):
    while i >= 0:
        if matrix[i][j] == "S":
            return True
        if matrix[i][j] == "O":
            return False
        i -= 1
    return False

def search_bottom(i, j):
    while i < N:
        if matrix[i][j] == "S":
            return True
        if matrix[i][j] == "O":
            return False
        i += 1
    return False

def search(i, j, direction):
    if direction == 0:
        return search_left(i, j)
    elif direction == 1:
        return search_right(i, j)
    elif direction == 2:
        return search_top(i, j)
    else:
        return search_bottom(i, j)

def search_students():
    # 동서남북으로 계속 보낸다.
    for ti, tj in teachers:
        for direction in range(4):
            if search(ti, tj, direction):
                # 학생을 만났다면 return True
                return True
    return False

def solution():
    for combi in empties_combinations:
        #일단 벽을 세워본다.
        for i, j in combi:
            matrix[i][j] = "O"
        #학생을 만나지 않았다면 return True
        if not search_students():
            return True
        #다시 벽을 없앤다.
        for i, j in combi:
            matrix[i][j] = "X"
    #여기까지오면 벽을 만들 수 없으니 print("NO")
    return False

print("YES") if solution() else print("NO")