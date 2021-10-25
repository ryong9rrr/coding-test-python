import sys
input = lambda : sys.stdin.readline().rstrip()

n = input()

num = "".join(sorted(n, reverse=True))

s = 0
for i in range(len(n)):
    s += int(n[i])

if num[-1] == "0" and s % 3 == 0:
    print(num)
else:
    print(-1)