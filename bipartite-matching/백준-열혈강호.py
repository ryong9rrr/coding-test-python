# nomalize Bipartite-matching algorithm
# 63840KB, 5976ms
from collections import defaultdict
MAX = 1001
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = defaultdict(list)
d = [0] * MAX

n, m = map(int, input().rstrip().split())
for i in range(1, n + 1):
    _input = list(map(int, input().rstrip().split()))
    nodes = _input[1:]
    for node in nodes:
        graph[i].append(node)

def dfs(x:int, c:list)->bool:
    for node in graph[x]:
        if c[node]:
            continue
        c[node] = True
        if d[node] == 0 or dfs(d[node], c):
            d[node] = x
            return True
    return False

count = 0
for i in range(1, n + 1):
    c = [False] * MAX
    if dfs(i, c):
        count += 1

print(count)

###########################################################
# Hopcroft-Karf
# 62588KB, 444ms

import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
INF = sys.maxsize

def bfs()->bool:
    q = deque()
    for a in range(1, n + 1):
        if not groupA[a]:
            dist[a] = 0
            q.append(a)
        else:
            dist[a] = INF

    dist[0] = INF
    while q:
        a = q.popleft()
        if dist[a] < dist[0]:
            for b in graph[a]:
                if dist[groupB[b]] == INF:
                    dist[groupB[b]] = dist[a] + 1
                    q.append(groupB[b])
    return dist[0] != INF

def dfs(a:int)->int:
    if a:
        for b in graph[a]:
            if dist[groupB[b]] == dist[a] + 1 and dfs(groupB[b]):
                groupA[a] = b
                groupB[b] = a
                return 1
        dist[a] = INF
        return 0
    return 1

n, m = map(int, input().split())
graph = [[]]

for i in range(n):
    graph.append(list(map(int, input().split()))[1:])

groupA = [0 for _ in range(n + 1)]
groupB = [0 for _ in range(m + 1)]
dist = [INF for _ in range(n + 1)]
match = 0
while bfs():
    for a in range(1, n + 1):
        if not groupA[a]:
            match += dfs(a)

print(match)