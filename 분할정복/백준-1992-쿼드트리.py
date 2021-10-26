import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input())

def solve(n, i, j):
    if n == 1:
        return matrix[i][j]
    a = solve(n//2, i, j)
    b = solve(n//2, i, j + n//2)
    c = solve(n//2, i + n//2, j)
    d = solve(n//2, i + n//2, j + n//2)
    if a == b and a == c and a == d and len(a) == 1:
        return a
    else:
        return "(" + a + b + c + d + ")"

print(solve(n, 0, 0))