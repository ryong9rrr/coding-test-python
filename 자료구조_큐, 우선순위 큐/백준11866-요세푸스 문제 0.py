"""
원형 큐 문제
"""

import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

n, k = map(int, input().split())
cq = deque()
for i in range(1, n + 1):
    cq.append(i)

result = []
while cq:
    # 양수값은 시계방향, 음수값은 반시계방향
    cq.rotate(1 - k)
    result.append(str(cq.popleft()))

print(f"<{', '.join(result)}>")