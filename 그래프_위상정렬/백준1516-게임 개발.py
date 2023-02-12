from collections import defaultdict, deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# 그래프, 차수, value 정보 구성
graph = defaultdict(list)
degree = [0] * (n + 1)
times = [0] * (n + 1)
for v in range(1, n + 1):
    data = list(map(int, input().split()))
    times[v] = data[0]
    degree[v] += len(data[1:-1])
    for node in data[1:-1]:
        graph[node].append(v)

# 큐에 차수가 1인 노드만 일단 담고 result 초기화
result = [0] * (n + 1)
q = deque()
for v in range(1, n + 1):
    if degree[v] == 0:
        result[v] = times[v]
        q.append(v)

# 큐를 순회하며 result를 갱신하고 차수(degree)를 줄여준다.
while q:
    v = q.popleft()
    for node in graph[v]:
        result[node] = max(result[node], result[v] + times[node])
        degree[node] -= 1
        if degree[node] == 0:
            q.append(node)

# 정답 출력
for i in result[1:]:
    print(i)