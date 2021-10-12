import sys
input = sys.stdin.readline

array = []

n = int(input())
for _ in range(n):
    s = input().rstrip()
    array.append(s)

result = sorted(array, key = lambda x: (len(x), x))

for i in range(0, n):
    if i > 0 and result[i] == result[i-1]:
        continue
    print(result[i])