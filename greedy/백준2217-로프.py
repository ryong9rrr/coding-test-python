import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
roap = []
for _ in range(n):
    roap.append(int(input()))

roap.sort()
result = 0
for i in range(n):
    result = max(result, roap[i] * (n - i))

print(result)