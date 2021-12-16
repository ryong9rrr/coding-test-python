# 내 방법
import sys
input = lambda : sys.stdin.readline().rstrip()

s = input()
count = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1
print((count + 1) // 2)


# 이코테
import sys
input = lambda : sys.stdin.readline().rstrip()

s = input()
count0 = count1 = 0

if s[0] == "1":
    count0 += 1
else:
    count1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == "1":
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))