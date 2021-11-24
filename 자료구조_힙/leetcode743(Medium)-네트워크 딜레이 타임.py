"""
다익스트라 알고리즘, 우선순위 큐

1. 모든 노드가 신호를 받는데 걸리는 시간
2. 모든 노드에 도달할 수 있는지 여부(모든 노드에 도달할 수 없다면 -1 리턴)

node정보(times), 노드의 개수(n), 시작노드(k)가 주어진다.
"""
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 그래프 정보 초기화
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 노드: 거리 // 형태로 가장 최단거리만 담음
        dist = collections.defaultdict(int)
        q = [(0, k)]
        
        while q:
            time, node = heapq.heappop(q)
            # 가장 최소값부터 확인하므로 dist에는 최단거리만 들어가게 됨
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    # 거리 갱신
                    alt = time + w
                    heapq.heappush(q, (alt, v))
                    
        # dist의 길이가 전체 노드 개수와 같다면 모든 노드를 방문할 수 있다는 것
        if len(dist) == n:
            return max(dist.values())
        return -1