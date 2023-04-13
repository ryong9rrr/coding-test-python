# 접근 1 : 가장 기본적인 O(N^2), 160ms
import sys
input = lambda: sys.stdin.readline().rstrip()

# input
n = int(input())
numbers = list(map(int, input().split()))

# LIS
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# 접근 2 : 약간 최적화된 O(N^2), 140ms
import sys
input = lambda: sys.stdin.readline().rstrip()

# input
n = int(input())
numbers = list(map(int, input().split()))

# LIS
numbers = [0] + numbers
dp = [0] * len(numbers)
for i in range(1, len(numbers)):
    cur = numbers[i]
    max_value = -sys.maxsize
    for j in range(i):
        if cur > numbers[j]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1

print(max(dp))




# 접근 3 - 이분탐색 LIS, O(NlogN) : 48ms
from bisect import bisect_left
import sys
input = lambda: sys.stdin.readline().rstrip()

# input
n = int(input())
numbers = list(map(int, input().split()))

# 이분탐색 LIS
dp = [numbers[0]]
for i in range(1, len(numbers)):
    cur = numbers[i]
    if cur > dp[-1]:
        dp.append(cur)
    else:
        index = bisect_left(dp, cur)
        dp[index] = cur

print(len(dp))