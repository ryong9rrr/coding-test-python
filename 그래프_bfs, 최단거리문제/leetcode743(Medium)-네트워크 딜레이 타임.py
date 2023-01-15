"""
다익스트라 알고리즘, 우선순위 큐

1. 모든 노드가 신호를 받는데 걸리는 시간
2. 모든 노드에 도달할 수 있는지 여부(모든 노드에 도달할 수 없다면 -1 리턴)

node정보(times), 노드의 개수(n), 시작노드(k)가 주어진다.
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v, w, cost in times:
            graph[v].append((cost, w))
        
        dist = collections.defaultdict(int)
        q = [(0, k)]

        while q:
            time, v = heapq.heappop(q)
            if v not in dist:
                dist[v] = time
                for cost, w in graph[v]:
                    alt = time + cost
                    heapq.heappush(q, (alt, w))
        
        result = dist.values()

        if len(result) != n:
            return -1
        return max(result)