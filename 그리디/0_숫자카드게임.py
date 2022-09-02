import sys
input = lambda : sys.stdin.readline().rstrip()

matrix = []

n, m = map(int, input().split())
for _ in range(n):
    matrix.append(list(map(int, input().split())))

result = 0

for row in matrix:
    result = max(result, min(row))

print(result)

# 좀 더 간결하게
import sys
input = lambda : sys.stdin.readline().rstrip()

result = 0

n, m = map(int, input().split())
for _ in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)