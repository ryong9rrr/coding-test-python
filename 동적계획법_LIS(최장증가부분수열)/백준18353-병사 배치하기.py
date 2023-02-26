# 일반 LIS (672ms)
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
input_numbers = list(map(int, input().split()))

input_numbers.reverse()

def LIS(numbers):
    n = len(numbers)
    DP = [1] * n
    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                DP[i] = max(DP[i], DP[j] + 1)
    return max(DP)

lis = LIS(input_numbers)

print(N - lis)

# binary LIS (72ms)
import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left

N = int(input())
input_numbers = list(map(int, input().split()))
input_numbers.reverse()

def binary_LIS(numbers):
    DP = [numbers[0]]
    for i in range(1, len(numbers)):
        target = numbers[i]
        if target > DP[-1]:
            DP.append(target)
        else:
            idx = bisect_left(DP, target)
            DP[idx] = target
    return len(DP)

lis = binary_LIS(input_numbers)

print(N - lis)