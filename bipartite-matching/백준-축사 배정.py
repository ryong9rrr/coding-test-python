from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = 201

graph = defaultdict(list)

# input
n, m = map(int, input().rstrip().split())
for i in range(1, n + 1):
    _input = list(map(int, input().rstrip().split()))
    nodes = _input[1:]
    for node in nodes:
        graph[i].append(node)

d = [0] * (m + 1)

def dfs(x:int, c:list)->bool:
    for node in graph[x]:
        if c[node]:
            continue
        c[node] = True
        if d[node] == 0 or dfs(d[node], c):
            d[node] = x
            return True
    return False

# output
count = 0
for i in range(1, n+1):
    c = [False] * (m + 1)
    if dfs(i, c):
        count += 1

print(count)