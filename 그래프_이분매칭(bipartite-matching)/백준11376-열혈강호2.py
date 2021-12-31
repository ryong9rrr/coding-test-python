# nomalize Bipartite-matching Algorithm // 시간초과
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

def dfs(v, visited):
    for node in graph[v]:
        if visited[node]:
            continue
        visited[node] = True
        if not result[node] or dfs(result[node], visited):
            result[node] = v
            return True
    return False

match = 0
for _ in range(2):
    for v in range(1, n + 1):
        visited = [False] * (m + 1)
        if dfs(v, visited):
            match += 1

print(match)

#########################################
# HopCroft-Karf // 628ms
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

# 2개의 일을 할 수 있으므로 배열형태로 초기화
group_A = [[] for _ in range(n + 1)]
group_B = [0 for _ in range(m + 1)]
dist = [INF for _ in range(n + 1)]

def bfs()->bool:
    q = deque()
    for a in range(1, n + 1):
        if len(group_A[a]) < 2:
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
                # 배열이므로 append
                group_A[a].append(b)
                group_B[b] = a
                return 1
        dist[a] = INF
        return 0
    return 1

match = 0
while bfs():
    for a in range(1, n + 1):
        # 2번 확인
        if len(group_A[a]) < 2:
            match += dfs(a)
        if len(group_A[a]) < 2:
            match += dfs(a)

print(match)