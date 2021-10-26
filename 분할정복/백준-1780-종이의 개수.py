import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split())

number = {
    "-1": 0,
    "0": 0,
    "1": 0
}

def dnc(n:int, x:int, y:int):
    global number

    target = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if target != matrix[i][j]:
                target = -2

    if target == -2:
        n = n // 3
        dnc(n, x, y)
        dnc(n, x, y + n)
        dnc(n, x, y + 2 * n)
        dnc(n, x + n, y)
        dnc(n, x + n, y + n)
        dnc(n, x + n, y + 2 * n)
        dnc(n, x + 2 * n, y)
        dnc(n, x + 2 * n, y + n)
        dnc(n, x + 2 * n, y + 2 * n)
    else:
        number[target] += 1

dnc(n, 0, 0)

for value in number.values():
    print(value)