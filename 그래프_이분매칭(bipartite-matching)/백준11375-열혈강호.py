# nomalize Bipartite-matching algorithm
# 63840KB, 5976ms
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

graph = defaultdict(list)

n, m = map(int, input().split())
for v in range(1, n + 1):
    data = list(map(int, input().split()))
    graph[v] = data[1:]

result = [0] * (m + 1)

def dfs(v:int, visited:list)->bool:
    for node in graph[v]:
        if visited[node]:
            continue
        visited[node] = True
        if not result[node] or dfs(result[node], visited):
            result[node] = v
            return True
    return False

count = 0
for v in range(1, n + 1):
    visited = [False] * (m + 1)
    if dfs(v, visited):
        count += 1

print(count)

###########################################################
# Hopcroft-Karf
# 62588KB, 444ms

from collections import defaultdict, deque
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
INF = sys.maxsize

graph = defaultdict(list)

n, m = map(int, input().split())
for v in range(1, n + 1):
    data = list(map(int, input().split()))
    graph[v] = data[1:]

group_A = [0 for _ in range(n + 1)]
group_B = [0 for _ in range(m + 1)]
dist = [INF for _ in range(n + 1)]

def bfs()->bool:
    q = deque()
    for a in range(1, n + 1):
        if not group_A[a]:
            dist[a] = 0
            q.append(a)
        else:
            dist[a] = INF
    dist[0] = INF
    while q:
        a = q.popleft()
        if dist[a] < dist[0]:
            for b in graph[a]:
                if dist[group_B[b]] == INF:
                    dist[group_B[b]] = dist[a] + 1
                    q.append(group_B[b])
    return dist[0] != INF

def dfs(a):
    if a:
        for b in graph[a]:
            if dist[group_B[b]] == dist[a] + 1 and \
                dfs(group_B[b]):
                group_A[a] = b
                group_B[b] = a
                return 1
        dist[a] = INF
        return 0
    return 1

match = 0
while bfs():
    for a in range(1, n + 1):
        if not group_A[a]:
            match += dfs(a)

print(match)