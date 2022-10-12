
# 이코테 풀이
# 34040KB	188ms
import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
DP = []
for _ in range(N):
    DP.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = DP[i - 1][j - 1]
        if i == j:
            up = 0
        else:
            up = DP[i - 1][j]
        DP[i][j] = DP[i][j] + max(up_left, up)

print(max(DP[-1]))


# 나의 풀이
# 34040KB	216ms
import sys
input = lambda: sys.stdin.readline().rstrip()

def search_prev_max_value(i, j, DP):
    max_value = 0
    for d in [-1, 0]:
        pj = j + d
        if 0 <= pj < i:
            max_value = max(max_value, DP[i - 1][pj])
    return max_value

N = int(input())
DP = []
for i in range(N):
    DP.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        DP[i][j] = DP[i][j] + search_prev_max_value(i, j, DP)

print(max(DP[-1]))