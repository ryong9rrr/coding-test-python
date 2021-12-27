import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

array = list(map(int, input().split()))

weight = sorted(array)

target = 1
for i in range(0, n):
    if target < weight[i]:
        break
    target += weight[i]

print(target)