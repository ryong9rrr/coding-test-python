import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

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

V, E = map(int, input().split())
array = []
for _ in range(E):
    v, w, c = map(int, input().split())
    array.append((c, v, w))

array.sort()
parent = [x for x in range(V + 1)]
result = 0
for c, v, w in array:
    if find_parent(parent, v) != find_parent(parent, w):
        union_parent(parent, v, w)
        result += c

print(result)