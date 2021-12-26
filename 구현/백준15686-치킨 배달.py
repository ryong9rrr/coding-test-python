import itertools
import sys
input = lambda: sys.stdin.readline().rstrip()

def get_distance(houses, combinations):
    result = 0
    for hx, hy in houses:
        temp = sys.maxsize
        for cx, cy in combinations:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

matrix = []
N, M = map(int, input().split())
for _ in range(N):
    matrix.append(list(map(int, input().split())))

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            houses.append((i + 1, j + 1))
        elif matrix[i][j] == 2:
            chickens.append((i + 1, j + 1))

nCr = list(itertools.combinations(chickens, M))

result = sys.maxsize
for combinations in nCr:
    result = min(result, get_distance(houses, combinations))

print(result)