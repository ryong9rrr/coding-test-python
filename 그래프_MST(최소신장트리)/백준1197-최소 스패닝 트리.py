# 376ms
import sys
input = lambda:sys.stdin.readline().rstrip()
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
parent = [x for x in range(V + 1)]
data = []
for _ in range(E):
    v, w, value = map(int, input().split())
    data.append((value, v, w))
data.sort()

result = 0
for value, v, w in data:
    if find_parent(parent, v) != find_parent(parent, w):
        union_parent(parent, v, w)
        result += value

print(result)


# 힙 이용 // 460ms
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()
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

v, e = map(int, input().split())
parent = [x for x in range(v + 1)]
heap = []
for _ in range(e):
    v, w, value = map(int, input().split())
    heapq.heappush(heap, (value, v, w))

result = 0
while heap:
    value, v, w = heapq.heappop(heap)
    if find_parent(parent, v) != find_parent(parent, w):
        union_parent(parent, v, w)
        result += value

print(result)