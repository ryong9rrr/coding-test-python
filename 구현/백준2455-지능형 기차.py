import sys
input = lambda : sys.stdin.readline().rstrip()

result = 0
_max = 0
for _ in range(4):
    a, b = map(int, input().split())
    x = b - a
    result += x
    if _max < result:
        _max = result

print(_max)