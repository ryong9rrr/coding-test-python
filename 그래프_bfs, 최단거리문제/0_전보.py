"""
유향그래프, 비용이 있는 최단거리문제 -> 다익스트라문제

한 도시에서 갈 수 있는 모든 도시까지의 최단거리를 구하고 도시들에 도달 할 수 있는 총 비용,

--입력예시--
도시의 개수, 간선의 개수, 시작 도시
노드1 노드2 비용...
--출력--
메세지를 받을 수 있는 도시의 개수, 걸리는 시간

(3개도시, 간선2개, 시작도시는 1)
(도시 1에서 2로 가는 비용은 4, 1에서 3으로가는 비용은 2)
3 2 1
1 2 4
1 3 2
-> 2 4
"""
from collections import defaultdict, deque
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

n, m, startNode = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = defaultdict(int)
def dikjstra(startNode:int):
    heap = [(0, startNode)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node not in dist:
            dist[node] = cost
            for v, w in graph[node]:
                if v in dist:
                    continue
                alt = w + cost
                heapq.heappush(heap, (alt, v))

dikjstra(startNode)

if len(dist) <= 1:
    print(-1)
else:
    print( len(dist) - 1, max(dist.values()) )