import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(input())

result = ""
distance = 0
for i in range(m):
    d = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    for j in range(n):
        d[array[j][i]] += 1
    # 최대 value값을 갖는 key
    result += max(d, key=d.get)
    # 최대 value 값
    distance += n - max(d.values())

print(result, distance, sep="\n")