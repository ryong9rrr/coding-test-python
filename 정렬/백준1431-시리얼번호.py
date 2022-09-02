import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

def get_sum(strings):
    _sum = 0
    for string in strings:
        # if ord("0") <= ord(s) <= ord("9"):
        if string.isdigit():
            _sum += int(string)
    return _sum

arr.sort(key=lambda x:(len(x), get_sum(x), x))

for i in arr:
    print(i)