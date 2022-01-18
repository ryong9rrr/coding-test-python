import sys
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

n, m = map(int, input().split())
parent = [x for x in range(n + 1)]
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

for _type, a, b in data:
    if _type == 0:
        union_parent(parent, a, b)
    elif _type == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")