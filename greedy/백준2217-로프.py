import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

roap = []

for _ in range(n):
    roap.append(int(input()))

r = sorted(roap)
max = 0
for i in range(n):
    if max < r[i] * (n-i):
        max = r[i] * (n-i)

print(max)