# 일반적 이분매칭 알고리즘, input 정보를 바탕으로 
# graph를 구현하는 것이 관건이었음.

from itertools import combinations
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def dfs(v, visited):
    for node in graph[v]:
        if visited[node]:
            continue
        visited[node] = True
        if not result[node] or dfs(result[node], visited):
            result[node] = v
            return True
    return False

# 스탯에 대한 딕셔너리 테이블을 구성하고 입력받기
stats = defaultdict(list)
n = int(input())
for v in range(1, n + 1):
    data = list(map(int, input().split()))
    stats[v] = data

# 그래프를 구성하고
graph = defaultdict(list)
"""
조합식을 쓰지 않는다면
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ...
"""
# n마리의 상어 중 2마리를 고르는 조합
nCr = list(combinations(stats.keys(), 2))
for a, b in nCr:
    a1, a2, a3 = stats[a]
    b1, b2, b3 = stats[b]
    # 상어가 서로 잡아먹을 수 있어도 사이클이 있을 수는 없으므로 if ~ elif
    if a1 == b1 and a2 == b2 and a3 == b3:
        graph[a].append(b)
    elif a1 >= b1 and a2 >= b2 and a3 >= b3:
        graph[a].append(b)
    elif a1 <= b1 and a2 <= b2 and a3 <= b3:
        graph[b].append(a)

result = [0] * (n + 1)
count = 0
# 최대 2마리만 잡아 먹을 수 있으니
for _ in range(2):
    for v in range(1, n + 1):
        visited = [False] * (n + 1)
        if dfs(v, visited):
            count += 1

print(n - count)