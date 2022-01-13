"""
<중국인의 나머지 정리> 문제

숫자 범위가 작아서 브루트포스로 풀었지만 나중에 정수론으로 풀어보자
"""

import sys
input = lambda : sys.stdin.readline().rstrip()

E, S, M = map(int, input().split())

"""
1 <= E <= 15
1 <= S <= 28
1 <= M <= 19
"""
year = e = s = m = 1

while not (e == E and s == S and m == M):
    year += 1
    e += 1
    s += 1
    m += 1

    if e > 15: e = 1
    if s > 28: s = 1
    if m > 19: m = 1

print(year)