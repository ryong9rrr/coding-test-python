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


# 22년 9월 풀이
N, K = map(int, input().split())
data = []
for _ in range(N):
    i = int(input())
    if K >= i:
        data.append(i)

data.sort(reverse = True)

count = 0
for i in data:
    if K <= 0:
        break
    if K < i:
        continue
    a, b = divmod(K, i)
    count += a
    K = b

print(count)