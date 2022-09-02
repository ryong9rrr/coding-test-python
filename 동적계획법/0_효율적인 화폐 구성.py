"""
[INPUT]
2 15
2
3
[OUTPUT]
5

[INPUT]
3 4
3
5
7
[OUTPUT]
-1
"""
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

INF = int(1e9)
d = [INF] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])