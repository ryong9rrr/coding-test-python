# 시간초과 (탑-다운 방식)
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

m = 1000000007

d = [0] * 1000001
def dp(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    if x == 2:
        return 7
    if d[x]:
        return d[x]
    d[x] = 3 * dp(x - 2) + 2 * dp(x - 1)
    for i in range(3, x + 1):
        d[x] += (2 * dp(x - i)) % m
    d[x] %= m
    return d[x]

n = int(input())
print(dp(n))

# 시간초과 (바텀 업 방식)
import sys
input = lambda: sys.stdin.readline().rstrip()

m = 1000000007

def dp(x):
    d = [0] * 1000001
    d[:3] = [1, 2, 7]
    for i in range(3, x + 1):
        d[i] = 3 * d[i - 2] + 2 * d[i - 1]
        for j in range(i - 3, -1, -1):
            d[i] += (2 * d[j]) % m
        d[i] %= m
    return d[x]

n = int(input())
print(dp(n))

# 2차원 행렬로 메모리 절약
import sys
input = lambda: sys.stdin.readline().rstrip()

m = 1000000007
def dp(x):
    d = [[0, 0] for _ in range(1000001)]
    d[0][0], d[1][0], d[2][0] = 1, 2, 7
    for i in range(3, x + 1):
        d[i][1] = (d[i - 3][0] + d[i - 1][1]) % m
        d[i][0] = (2 * d[i - 1][0] + 3 * d[i - 2][0] + 2 * d[i][1]) % m
    return d[x][0]

n = int(input())
print(dp(n))