# 내 방법
import sys
input = lambda : sys.stdin.readline().rstrip()

s = input()
count = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1
print((count + 1) // 2)


# 이코테 풀이
import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()

bundle_0 = bundle_1 = 0

if s[0] == "0":
    bundle_0 += 1
else:
    bundle_1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == "0":
            bundle_0 += 1
        else:
            bundle_1 += 1

print(min(bundle_0, bundle_1))