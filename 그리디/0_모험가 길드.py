"""
[INPUT]
5
2 3 1 2 2
[OUTPUT]
2
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

data.sort()
result = count = 0
for num in data:
    count += 1
    if count >= num:
        result += 1
        count = 0

print(result)