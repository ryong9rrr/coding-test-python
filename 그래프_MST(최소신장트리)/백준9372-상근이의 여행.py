"""
문제를 잘 읽어보면 그냥 간선의 수를 구하는 문제... ㅋ
문제에서 모든 노드는 연결되어있다고 했다. 그러면 무조건 
하나의 집합이라는 소리고 그렇다면 최소신장트리에서 간선의 수는?
당연히 노드의 수 - 1
"""
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

T = int(input())
result = []
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    result.append(n - 1)

for i in result:
    print(i)

"""
하지만 문제의 의도대로 한번 풀어보자.
"""
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    x, y = find_parent(parent, a), find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())
result = []
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    parent = [x for x in range(n + 1)]
    for v in range(1, n + 1):
        for node in graph[v]:
            if find_parent(parent, v) != find_parent(parent, node):
                union_parent(parent, v, node)
    cnt = 0
    for i in range(1, n + 1):
        if parent[i]:
            cnt += 1
    result.append(cnt)
# 어차피 모든 노드는 연결되어있기 때문에 -1 해서 간선의 수를 세어주는 건 변함이 없음...
for ans in result:
    print(ans - 1)