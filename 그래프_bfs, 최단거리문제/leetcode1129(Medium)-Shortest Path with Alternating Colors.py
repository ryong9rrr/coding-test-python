# 88ms(77.86%), 14.2MB(73.17%)
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        INF = int(1e9)
        RED = 0
        BLUE = 1
        graph = collections.defaultdict(list)
        for v, w in redEdges:
            graph[v].append([w, RED])
        for v, w in blueEdges:
            graph[v].append([w, BLUE])

        visited = [[False, False] for _ in range(n)]
        answer = [INF] * n
        answer[0] = 0
        q = collections.deque()
        # start to 0 Node
        for w, color in graph[0]:
            visited[0][color] = True
            q.append([0, None, 0]) # node, unknown-color, dist
        
        # BFS
        while q:
            v, prev_color, dist = q.popleft()
            for w, color in graph[v]:
                if color != prev_color and not visited[w][color]:
                    visited[w][color] = True
                    q.append([w, color, dist + 1])
                    answer[w] = min(answer[w], dist + 1)
        
        # if element is INF, not path.
        return [-1 if x == INF else x for x in answer]