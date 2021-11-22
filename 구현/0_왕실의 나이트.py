import sys
input = lambda : sys.stdin.readline().rstrip()

location = input()
m = int(ord(location[0])) - int(ord("a")) + 1
n = int(location[1])

#size: 8 x 8
#상하좌우
steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

result = 0
#한번의 이동만 보면 되는 문제..
for step in steps:
    y, x = step
    nm, nn = m + y, n + x
    if nm >= 1 and nn >= 1 and nm <= 8 and nn <= 8:
        result += 1

print(result)
"""
a1
-> 2

c2
-> 6
"""