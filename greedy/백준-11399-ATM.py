import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

people = list(map(int, input().split()))

result = 0
p = sorted(people)
for i in range(n):
    result += p[i] * (n - i)

print(result)