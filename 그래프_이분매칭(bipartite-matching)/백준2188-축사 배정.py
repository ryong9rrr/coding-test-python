from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

graph = defaultdict(list)

n, m = map(int, input().split())
# 그래프 초기화
for v in range(1, n + 1):
    data = list(map(int, input().split()))
    graph[v] = data[1:]

# 전체 결과를 담은 전역변수
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

count = 0
for v in range(1, n + 1):
    visited = [False] * (m + 1)
    if dfs(v, visited):
        count += 1

print(count)