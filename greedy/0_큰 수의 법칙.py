# 단순 반복
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

first, second = numbers[-1], numbers[-2]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 수학적접근(규칙찾기)으로 최적화
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

first, second = numbers[-1], numbers[-2]

cycle, mod = divmod(m, k + 1)
count = cycle * k + mod

result = count * first + (m - count) * second

print(result)