money = 1000 - int(input())
result = 0

result += money // 500
money %= 500

result += money // 100
money %= 100

result += money // 50
money %= 50

result += money // 10
money %= 10

result += money // 5
money %= 5

result += money

print(result)


##################################################

import sys
input = lambda: sys.stdin.readline().rstrip()

money_table = [500, 100, 50, 10, 5, 1]
# 거스름돈
money = 1000 - int(input())

result = 0
for m in money_table:
    a, b = divmod(money, m)
    result += a
    money = b

print(result)