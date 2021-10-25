import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

array = [0] + list(map(int, input().split()))

d = [0] * (n + 1)

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if count == array[i] and d[j] == 0:
            d[j] = i
            break
        if d[j] == 0:
            count += 1

print(*d[1:])