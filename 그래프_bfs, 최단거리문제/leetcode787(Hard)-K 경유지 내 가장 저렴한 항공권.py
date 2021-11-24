# 다익스트라 // 100~150ms
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
        INF = int(1e9)
        nodeInfo = [(INF, k)] * n
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        q = [(0, src, k)]
        
        while q:
            price, node, count = heappop(q)
            if node == dst:
                return price
            if count >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt <= nodeInfo[v][0] or count > nodeInfo[v][1] :
                        nodeInfo[v] = (alt, count - 1)
                        heappush(q, (alt, v, count - 1))
                    
        return -1
                

# 다른 방법
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