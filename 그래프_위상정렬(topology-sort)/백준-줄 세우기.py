from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def topological_sort(graph:dict, degree:list)->list:
    result = []
    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        result.append(x)
        for node in graph[x]:
            degree[node] -= 1
            if degree[node] == 0:
                q.append(node)

    return result


n, m = map(int, input().rstrip().split())

graph = defaultdict(list)
degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # exception error
    if a > n or b > n:
        print("input range error")
    graph[a].append(b)
    degree[b] += 1

result = topological_sort(graph, degree)
for i in result:
    print(i, end=" ")