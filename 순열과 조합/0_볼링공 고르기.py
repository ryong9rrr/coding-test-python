"""
5 3
1 3 2 3 2
-> 8

8 5
1 5 4 3 2 4 5 2
-> 25
"""
from collections import Counter
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = list(map(int, input().split()))

counts = Counter(array)
result = 0
for key in sorted(counts.keys()):
    n -= counts[key]
    result += counts[key] * n

print(result)