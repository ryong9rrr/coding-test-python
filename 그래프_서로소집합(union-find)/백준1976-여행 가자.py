import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
paths = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n):
        if array[i][j]:
            graph[i + 1].append(j + 1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    x, y = find_parent(parent, a), find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

parent = [x for x in range(n + 1)]

for v in range(1, n + 1):
    for node in graph[v]:
        if find_parent(parent, v) != find_parent(parent, node):
            union_parent(parent, v, node)

result = find_parent(parent, paths[0])

def solve():
    for path in paths:
        if result != find_parent(parent, path):
            return "NO"
    return "YES"

print(solve())