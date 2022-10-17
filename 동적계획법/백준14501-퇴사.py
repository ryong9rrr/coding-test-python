# 뒤에서부터 DP
# 30840KB	68ms
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
table = []
for _ in range(N):
    cost, profit = map(int, input().split())
    table.append([cost, profit])

max_value = 0
DP = [0] * (N + 1)

for day in range(N - 1, -1, -1):
    cost, profit = table[day]
    if day + cost > N:
        DP[day] = max_value
    else:
        max_value = DP[day] = max(max_value, profit + DP[day + cost])

print(max_value)