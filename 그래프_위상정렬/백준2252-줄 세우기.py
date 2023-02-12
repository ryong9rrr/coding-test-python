from collections import defaultdict, deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
# graph, 차수 정보 초기화
graph = defaultdict(list)
degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

# 차수가 0인 것만 q에 담기
q = deque()
for v in range(1, n + 1):
    if degree[v] == 0:
        q.append(v)

# 위상정렬 시작
result = []
while q:
    v = q.popleft()
    result.append(v)
    for node in graph[v]:
        degree[node] -= 1
        if degree[node] == 0:
            q.append(node)

print(*result)