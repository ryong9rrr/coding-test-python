# counting-sort

import sys
input = sys.stdin.readline

N = 10000
count = [0] * (N+1)

n = int(input())
for _ in range(n):
    x = int(input())
    count[x] += 1

for i in range(1, N+1):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)