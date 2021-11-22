# 완전탐색
import sys
input = lambda : sys.stdin.readline().rstrip()

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            time = "".join(list(map(str, [i, j, k])))
            if "3" in time:
                count += 1

print(count)

# 수리적으로 O(1)
import sys
input = lambda : sys.stdin.readline().rstrip()

h = int(input())

# 시간당 "3"이 포함된 횟수
count = 15 * 60 + 45 * 15

if h < 3:
    print( count * (h + 1) )
elif 3 <= h < 13:
    print( count * h + 3600 )
elif 13 <= h < 23:
    print( count * (h - 1) + 3600 * 2 )
else:
    print( count * (h - 2) + 3600 * 3 )