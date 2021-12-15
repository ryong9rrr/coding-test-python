from collections import defaultdict, deque
import sys
input = lambda :sys.stdin.readline().rstrip()

def topology_sort(graph:dict, indegree:list)->list:
    result = []
    q = deque()
    for v in range(1, n + 1):
        if indegree[v] == 0:
            q.append(v)
    while q:
        x = q.popleft()
        result.append(x)
        for v in graph[x]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return result

n, m = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (n + 1)
for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    indegree[w] += 1

result = topology_sort(graph, indegree)

print(*result)