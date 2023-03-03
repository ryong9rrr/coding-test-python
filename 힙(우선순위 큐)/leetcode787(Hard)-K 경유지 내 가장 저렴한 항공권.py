# 다익스트라 : 190ms(58.57%), 15.7MB(11.74%)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v, w, cost in flights:
            graph[v].append((w, cost))

        costs = [float('inf')] * n
        rests = [k] * n
        q = [(0, k, src)]

        while q:
            acc, rest, v = heapq.heappop(q)
            if v == dst:
                return acc
            if rest < 0:
                continue
            for w, cost in graph[v]:
                alt = acc + cost
                if alt < costs[w] or rests[w] < rest:
                    costs[w] = alt
                    rests[w] = rest - 1
                    heapq.heappush(q, (alt, rest - 1, w))

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