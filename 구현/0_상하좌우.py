import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
commands = input().split()

x, y = 1, 1
move_types = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

for command in commands:
    dx, dy = move_types[command]
    nx, ny = x + dx, y + dy
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
"""
5
R R R U D D
-> 3 4
"""