# 그래프를 딕셔너리로 만든 후 풀이
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

# 하지만 사실 단순히 이어져있다면 합쳐주고,
# 결국 parent에는 head 노드만 담기게 되기 때문에
# parent에 인덱스로만 접근해도 됨.
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

n = int(input())
m = int(input())
data = [[]]
for _ in range(n):
    data.append(list(map(int, input().split())))
paths = list(map(int, input().split()))

parent = [x for x in range(n + 1)]

# 연결되어있다고 한다면 연결시켜준다.
for v in range(1, n + 1):
    for w, is_connected in enumerate(data[v]):
        if is_connected:
            union_parent(parent, v, w + 1)

# 경로의 head가 모두 같아야 가능한 여행경로다.
def solve():
    for i in range(len(paths) - 1):
        if parent[paths[i]] != parent[paths[i + 1]]:
            return "NO"
    return "YES"

print(solve())