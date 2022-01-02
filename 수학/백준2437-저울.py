# 귀납법적 추론
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))

data.sort()

acc = 1
for number in data:
    if acc < number:
        break
    acc += number

print(acc)