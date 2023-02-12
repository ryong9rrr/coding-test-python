"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
from collections import deque
import copy
import sys
input = lambda : sys.stdin.readline().rstrip()

V = int(input())
indegree = [0] * (V + 1)
time = [0] * (V + 1)
graph = [[] for _ in range(V + 1)]

for i in range(1, V + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

result = topology_sort()

for i in range(1, V + 1):
    print(result[i])
"""
10
20
14
18
17
"""