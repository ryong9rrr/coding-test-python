"""
--input--
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7

--result--
12
5
"""

from collections import deque, defaultdict

a = defaultdict(list)
b = defaultdict(list)

n = int(input())

degree = [0] * (n + 1)
result = [0] * (n + 1)
c = [0] * (n + 1)

m = int(input())
for _ in range(m):
    node, next_node, time = map(int, input().split())
    a[node].append((next_node, time))
    b[next_node].append((node, time))
    degree[next_node] += 1
start, end = map(int, input().split())

def topology_sort(start:int, end:int):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for info in a[x]:
            node, time = info
            # 더 큰 값으로 갱신
            if result[node] <= time + result[x]:
                result[node] = time + result[x]
            degree[node] -= 1
            if degree[node] == 0:
                q.append(node)
    count = 0
    q.append(end)
    while q:
        x = q.popleft()
        for info in b[x]:
            node, time = info
            if result[x] - result[node] == time:
                count += 1
                if c[node] == 0:
                    q.append(node)
                    c[node] = 1
    print(result[end])
    print(count)

topology_sort(start, end)

#########################################################################
# 모든 경로를 찾은 후 그 경로를 바탕으로 값을 구함.. 하지만 graph가 matrix여서 메모리초과.
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# input data
n = int(input().rstrip())

graph = [[0] * (n + 1) for _ in range(n + 1)]

m = int(input().rstrip())
for _ in range(m):
    node, next_node, c = map(int, input().rstrip().split())
    graph[node][next_node] = c
start, end = map(int, input().rstrip().split())

visited = [False] * (n + 1)
# when all node is connected, from start to end
dq = deque()
paths = []
def dfs_all(v:int, goal:int):
    visited[v] = True
    dq.append(v)
    if v == goal:
        path = []
        for i in dq:
            path.append(i)
        paths.append(path)
        dq.pop()
        return
    for i in range(1, n+1):
        if graph[v][i] != 0 and not visited[i]:
            dfs_all(i, goal)
            visited[i] = False
    dq.pop()

dfs_all(start, end)
#print(graph)
#print(paths)

result = set([])
max_cost = 0
for path in paths:
    temp = set(path)
    cost = 0
    for i in range(0, len(path)-1):
        cost += graph[path[i]][path[i+1]]
    if max_cost <= cost:
        max_cost = cost
        result = result | temp

print(max_cost)
print(len(result))