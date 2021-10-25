import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())

A = []

for _ in range(N):
    A.append(int(input()))

result = 0
for i in range(N-1, -1, -1):
    result += K // A[i]
    K %= A[i]

print(result)