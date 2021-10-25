from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

graph = defaultdict(list)

V, E = map(int, input().split())

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

#print(graph)

d = [0] * (V + 1)
finished = [False] * (V + 1)
SCC = []
stack = deque()
# SCC 내에서 가장 높은 우선순위를 가진 노드를 강제하기 위해 id를 부여
_id = 0
def dfs(x:int)->int:
    # global로 선언해줘야한다..
    global _id
    _id += 1
    d[x] = _id
    stack.append(x)
    parent = d[x]
    for node in graph[x]:
        # 아직 방문하지 않은 이웃 노드인 경우
        if d[node] == 0:
            parent = min(parent, dfs(node))
        # 방문은 했지만 아직 처리중인 경우
        elif not finished[node]:
            parent = min(parent, d[node])

    if parent == d[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(sorted(scc))

    return parent

for i in range(1, V+1):
    if d[i] == 0:
        dfs(i)

l = len(SCC)
# key값 기준 정렬
sorted_SCC = sorted(SCC, key=lambda x: x[0])
print(l)
for list in sorted_SCC:
    # ES6의 spread 연산과 비슷
    print(*list, -1)