import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            houses.append([i + 1, j + 1])
        elif matrix[i][j] == 2:
            chickens.append([i + 1, j + 1])

chickens_combinations = list(itertools.combinations(chickens, M))

result = sys.maxsize
for chickens_combination in chickens_combinations:
    total = 0
    for hx, hy in houses:
        temp = sys.maxsize
        for cx, cy in chickens_combination:
            distance = abs(hx - cx) + abs(hy - cy)
            temp = min(temp, distance)
        total += temp
    result = min(result, total)

print(result)