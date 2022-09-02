# f(n) = 3 x f(n-2) + [ 2 x f(n-4) + 2 x f(n-6) ... + 2 x f(0) ]

d = [0] * 31
d[0:3] = [1, 0, 3]
def dp(x):
    if x > 2:
        for i in range(3, x+1):
            if i % 2 == 0:
                result = 3 * d[i - 2]
                j = 4
                while x-j >= 0:
                    result += 2 * d[i-j]
                    j += 2
                d[i] = result

n = int(input())
dp(n)
print(d[n])

# 더 직관적인
import sys
input = lambda: sys.stdin.readline().rstrip()

def dp(x):
    d = [0] * 31
    d[:3] = [1, 0, 3]
    for i in range(3, x + 1):
        if i % 2 == 0:
            d[i] = 3 * d[i - 2]
            for j in range(4, x + 1, 2):
                d[i] += 2 * d[i - j]
    return d[x]

n = int(input())
print(dp(n))