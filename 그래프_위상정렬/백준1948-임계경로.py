import heapq
from collections import defaultdict, deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

# 그래프와 역방향 그래프, 차수 테이블 초기화
graph = defaultdict(list)
reverse_graph = defaultdict(list)
degree = [0] * (n + 1)
for _ in range(m):
    a, b, value = map(int, input().split())
    graph[a].append((b, value))
    reverse_graph[b].append((a, value))
    degree[b] += 1

start, end = map(int, input().split())

# 큐에 먼저 start노드를 넣어서 노드로 가는 비용 리스트 초기화
result = [0] * (n + 1)
q = deque()
q.append(start)
while q:
    v = q.popleft()
    for node, value in graph[v]:
        result[node] = max(result[node], result[v] + value)
        degree[node] -= 1
        if not degree[node]:
            q.append(node)

# 역방향 추적
paths = [0] * (n + 1)
count = 0
q.append(end)
while q:
    v = q.popleft()
    for node, value in reverse_graph[v]:
        if result[v] - result[node] == value:
            count += 1
            if not paths[node]:
                q.append(node)
                # 방문한 순서 기록
                paths[node] = count

print(result[end])
print(count)