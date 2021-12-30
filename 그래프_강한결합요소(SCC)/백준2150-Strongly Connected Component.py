from collections import deque, defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

graph = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

stack = deque()
parents = [0] * (n + 1)
visited = [False] * (n + 1)
result_SCC = []
# SCC 내에서 가장 높은 우선순위를 가진 노드를 강제하기 위해 id를 부여
_id = 0
def dfs(v):
    global _id
    _id += 1
    # id값을 기록
    parents[v] = _id
    stack.append(v)
    parent = parents[v]
    for node in graph[v]:
        if parents[node] == 0:
            parent = min(parent, dfs(node))
        elif not visited[node]:
            parent = min(parent, parents[node])

    if parent == parents[v]:
        scc = []
        while True:
            x = stack.pop()
            scc.append(x)
            visited[x] = True
            if x == v:
                break
        result_SCC.append(sorted(scc))
    return parent

for v in range(1, n + 1):
    if parents[v] == 0:
        dfs(v)

print(len(result_SCC))
result_SCC.sort()
for scc in result_SCC:
    print(*sorted(scc), -1)