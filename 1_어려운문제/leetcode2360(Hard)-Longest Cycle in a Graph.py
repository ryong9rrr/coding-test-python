# 매우 어려운 문제... ㅠㅠ

"""
접근 1 (리트코드 솔루션 1) : DFS, 1469ms(45.80%), 141MB(52.65%)
- 시간복잡도, 공간복잡도 : O(N)
"""
class Solution:
    ans = -1

    def dfs(self, node, edges, dist, visited):
        neighbor = edges[node]
        if neighbor == -1:
            return
        
        if neighbor not in visited:
            dist[neighbor] = dist[node] + 1
            visited.add(neighbor)
            self.dfs(neighbor, edges, dist, visited)
            return

        if dist[neighbor]:
            self.ans = max(self.ans, dist[node] - dist[neighbor] + 1)
        
        
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dist = collections.defaultdict(int)
                dist[node] = 1
                self.dfs(node, edges, dist, visited)

        return self.ans
    

"""
접근 2 (리트코드 솔루션 2) : Kahn's Alogirhtm(위상정렬), 1199ms(88.16%), 34.7MB(82.24%)
- 시간복잡도, 공간복잡도 : O(N)
"""
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        indegree = [0] * n

        # Count indegree of each node.
        for w in edges:
            if w != -1:
                indegree[w] += 1

        # Kahn's algorithm(위상정렬) starts.
        q = collections.deque()
        for v in range(n):
            if indegree[v] == 0:
                q.append(v)

        while q:
            v = q.popleft()
            visited.add(v)
            w = edges[v]
            if w != -1:
                indegree[w] -= 1
                if indegree[w] == 0:
                    q.append(w)

        # 위상정렬을 완료한 뒤에 아직 방문처리되지 않은 노드들은 scc임
        ans = -1
        for v in range(n):
            if v not in visited:
                visited.add(v)
                w = edges[v]
                count = 1
                while v != w:
                    visited.add(w)
                    count += 1
                    w = edges[w]
                ans = max(ans, count)

        return ans