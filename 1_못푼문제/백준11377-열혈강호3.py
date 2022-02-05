# pypy로 제출하면 일반적인 이분매칭 알고리즘도 통과...
# 호프크로프트-카프 알고리즘으로 풀 수는 없을까?
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

def dfs(x):
    for node in graph[x]:
        if c[node]:
            continue
        c[node] = True
        if d[node] == 0 or dfs(d[node]):
            d[node] = x
            return True
    return False

graph = defaultdict(list)

n, m, k = map(int, input().split())
for i in range(1, n + 1):
    nodes = list(map(int, input().split()))[1:]
    for node in nodes:
        graph[i].append(node)

d = [0] * (m + 1)

count = 0
for i in range(1, n + 1):
    c = [False] * (m + 1)
    if dfs(i):
        count += 1

extra = 0
for i in range(1, n + 1):
    c = [False] * (m + 1)
    if dfs(i):
        extra += 1
    if extra >= k:
        break

print(count + extra)