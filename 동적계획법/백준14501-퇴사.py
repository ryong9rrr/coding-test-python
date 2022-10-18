# 뒤에서부터 DP
# 30840KB	68ms
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
table = []
for _ in range(N):
    cost, profit = map(int, input().split())
    table.append([cost, profit])

DP = [0] * (N + 1)
max_value = 0
# 맨 마지막날은 제낀다.
for day in range(N - 1, -1, -1):
    cost, profit = table[day]
    next_day = day + cost
    if next_day <= N:
        DP[day] = max(max_value, profit + DP[next_day])
        max_value = DP[day]
    else:
        DP[day] = max_value

print(max_value)