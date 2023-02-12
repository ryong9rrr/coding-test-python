# 접근 1 - dfs + 백트래킹 : O(N), 2027ms(69.78%) 159.3MB(75.39%)
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = collections.defaultdict(list)
        for v, w in roads:
            adj[v].append(w)
            adj[w].append(v)

        fuel = 0

        def dfs(node, parent):
            nonlocal fuel
            representatives = 1
            if not adj[node]:
                return representatives

            for child in adj[node]:
                if child != parent:
                    representatives += dfs(child, node)
                    
            if node != 0:
                fuel += math.ceil(representatives / seats)
            return representatives

        dfs(0, None)

        return fuel

# 접근 2 - 위상정렬(BFS) : 2079ms(53.58%), 55.4MB(98.44%)
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = collections.defaultdict(list)
        degrees = [0] * n
        for v, w in roads:
            adj[v].append(w)
            adj[w].append(v)
            degrees[v] += 1
            degrees[w] += 1 

        # 위상정렬(BFS)
        representatives = [1] * n
        q = collections.deque()
        for v in range(1, n):
            if degrees[v] == 1:
                q.append(v)

        fuel = 0
        while q:
            v = q.popleft()
            fuel += math.ceil(representatives[v] / seats)
            for w in adj[v]:
                degrees[w] -= 1
                representatives[w] += representatives[v]
                if w == 0:
                    continue
                if degrees[w] == 1:
                    q.append(w)
        
        return fuel