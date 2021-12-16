"""
[INPUT]
02984
[OUTPUT]
576

[INPUT]
567
[OUTPUT]
210
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()

s = list(map(int, list(S)))

result = 0

for num in s:
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)