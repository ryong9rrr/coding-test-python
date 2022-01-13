"""
배수판정법 + 그리디 문제
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

number = sorted(input(), reverse=True)

total = sum([int(num) for num in number])

if number[-1] == "0" and total % 3 == 0:
    print("".join(number))
else:
    print(-1)