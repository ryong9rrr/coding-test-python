# 전형적인 BFS, 프로그래머스Lv3-가장 먼 노드 문제와 동일하다.
import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)

distance = [-1] * (N + 1)

q = deque()
q.append(X)
distance[X] = 0

while q:
    v = q.popleft()
    for w in graph[v]:
        if distance[w] == -1:
            distance[w] = distance[v] + 1
            q.append(w)

result = []

for v in range(1, N + 1):
    if distance[v] == K:
        result.append(v)

if not result:
    print(-1)

for v in result:
    print(v)