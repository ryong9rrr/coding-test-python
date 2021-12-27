import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    if (m+1)//2 > 4:
        print(4)
    else:
        print((m+1)//2)
else:
    if m >= 7:
        print(m-2)
    else:
        print(min(4, m))