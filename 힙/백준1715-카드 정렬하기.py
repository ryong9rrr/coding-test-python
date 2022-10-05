# 33692KB	240ms
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
heapq.heapify(numbers)

total = 0

while len(numbers) > 1:
    a, b = heapq.heappop(numbers), heapq.heappop(numbers)
    total += a + b
    heapq.heappush(numbers, a + b)

print(total)