# 2168ms(28.16%), 151.4MB(13.79%)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        graph = {}
        for v, w in enumerate(edges):
            graph[v] = w

        def dfs(v, visited, dist, depth):
            visited[v] = True
            dist[v] = depth
            w = graph[v]
            if not visited[w] and w != -1:
                dfs(w, visited, dist, depth + 1)

        visited1 = [False] * N
        dist1 = [0] * N
        dfs(node1, visited1, dist1, 0)

        visited2 = [False] * N
        dist2 = [0] * N
        dfs(node2, visited2, dist2, 0)

        min_dist = float('inf')
        result = -1
        for v in range(N):
            current_max = max(dist1[v], dist2[v])
            if visited1[v] and visited2[v] and min_dist > current_max:
                min_dist = current_max
                result = v

        return result