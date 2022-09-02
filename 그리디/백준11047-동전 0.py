import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
money_table = []
for _ in range(n):
    money_table.append(int(input()))

# 가장 큰 단위부터 확인해야하므로
money_table.sort(reverse=True)

count = 0
for m in money_table:
    a, b = divmod(k, m)
    # 몫이 없다면 그냥 넘어감
    if not a:
        continue
    count += a
    k = b

print(count)