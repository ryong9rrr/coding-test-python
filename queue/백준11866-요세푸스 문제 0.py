"""
원형 큐 문제
"""

import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, K = map(int, input().split())

cq = deque()
for i in range(1, N + 1):
    cq.append(i)

result = []
while cq:
    # K가 3일 때.. 원형큐를 -2만큼 옮겨준다면 [1 2 3] -> [2 3 1] -> [3 2 1] 이렇게됨
    cq.rotate(-(K - 1))
    x = cq.popleft()
    result.append(x)

print("<", end="")
for i in range(0, N-1):
    print(f"{result[i]}, ", end="")
print(f"{result[-1]}>")