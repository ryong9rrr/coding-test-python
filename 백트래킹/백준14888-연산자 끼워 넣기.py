# DFS 백트래킹(이코테 풀이) 30840KB	104ms
# 아니 순열 풀이나 시간이 거기서 거기일 줄 알았는데 훨씬 빠르다...덜덜덜
import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)
N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -INF
min_result = INF

def dfs(i, acc):
    global max_result, min_result, add, sub, mul, div
    if i == N:
        max_result = max(max_result, acc)
        min_result = min(min_result, acc)
        return
    number = numbers[i]
    if add > 0:
        add -= 1
        dfs(i + 1, acc + number)
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, acc - number)
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, acc * number)
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, int(acc / number))
        div += 1

dfs(1, numbers[0])

print(max_result)
print(min_result)

# 이 문제는 순열로도 풀 수 있는데... python은 시간초과고 PyPy3로 통과했다.
# 근데 PyPy3로도 너무 느렸음. 670236KB	2500ms
import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)
N = int(input())
numbers = list(map(int, input().split()))
opers_n = list(map(int, input().split()))
opers_s = ["+", "-", "x", "%"]
operators = []
for i in range(4):
    for _ in range(opers_n[i]):
        operators.append(opers_s[i])

prods = list(permutations(operators, N - 1))

max_result = -INF
min_result = INF

for opers in prods:
    acc = numbers[0]
    for i in range(1, N):
        number = numbers[i]
        op = opers[i - 1]
        if op == "+":
            acc += number
        elif op == "-":
            acc -= number
        elif op == "x":
            acc *= number
        else:
            if acc < 0:
                acc = ((acc * (-1)) // number) * (-1)
            else:
                acc //= number
    max_result = max(max_result, acc)
    min_result = min(min_result, acc)

print(max_result)
print(min_result)