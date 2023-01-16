# 다익스트라 // 104ms
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        graph = collections.defaultdict(list)
        for v, w, cost in flights:
            graph[v].append((w, cost))

        costs = [INF] * n
        counts = [k] * n
        q = [(0, src, k)]
        
        while q:
            acc, v, count = heapq.heappop(q)
            if v == dst:
                return acc
            if count < 0:
                continue
            for w, cost in graph[v]:
                alt = acc + cost
                # 이미 갱신해놨던 정보보다 더 저렴하거나 넉넉하다면
                if alt < costs[w] or counts[w] < count:
                    costs[w] = alt
                    counts[w] = count - 1
                    heapq.heappush(q, (alt, w, count - 1))
        
        return -1

# 비슷한 방법
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        visited = defaultdict(set)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        q = [(0, src, k+1)]
        
        while q:
            price, node, count = heappop(q)
            if count in visited[node]:
                continue
            visited[node].add(count)
            if node == dst:
                return price
            if count > 0:
                count -= 1
                for v, w in graph[node]:
                    if count in visited[v]:
                        continue
                    heappush(q, (price + w, v, count))
        return -1