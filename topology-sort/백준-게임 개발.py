from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = defaultdict(list)
degree = [0] * (n + 1)
time = [0] * (n +1)

for i in range(n):
    _input = list(map(int, input().rstrip().split()))
    time[i+1] = _input[0]
    for node in _input[1:-1]:
        graph[node].append(i+1)
        degree[i+1] += 1

def topological_sort(graph:dict, time:list, degree:list)->list:
    result = [0] * (n + 1)
    q = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            result[i] = time[i]
            q.append(i)
    while q:
        x = q.popleft()
        for node in graph[x]:
            degree[node] -= 1
            result[node] = max(result[node], time[node] + result[x])
            if degree[node] == 0:
                q.append(node)

    return result

result = topological_sort(graph, time, degree)

for i in result[1:]:
    print(i)