"""
접근 1 : DFS 1, visited 집합 자료형을 사용하는 방법
- 시간복잡도 : O(N)
- 공간복잡도 : O(N)
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for v, w in connections:
            graph[v].append([w, 1])
            graph[w].append([v, 0])

        visited = set([0])
        count = 0
        def dfs(node):
            nonlocal count
            for child, sign in graph[node]:
                if child not in visited:
                    visited.add(child)
                    count += sign
                    dfs(child)

        dfs(0)

        return count
    
"""
접근 2 : DFS 2, visited를 사용하지 않고 파라미터 하나(부모 노드)를 더 받는 방법
- 시간복잡도 : O(N)
- 공간복잡도 : O(N)
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for v, w in connections:
            graph[v].append([w, 1])
            graph[w].append([v, 0])

        count = 0
        def dfs(parent, node):
            nonlocal count
            for child, sign in graph[node]:
                if parent != child:
                    count += sign
                    dfs(node, child)

        dfs(-1, 0) # 0번 노드의 부모 노드는 -1이라고 치고

        return count
    
"""
접근 3 : BFS, 접근 1과 동일(visited 사용)한데 DFS가 아닌 BFS로 푼 것임
- 시간복잡도 : O(N)
- 공간복잡도 : O(N)
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for v, w in connections:
            graph[v].append([w, 1])
            graph[w].append([v, 0])

        # BFS
        q = collections.deque([0])
        visited = set([0])
        count = 0
        while q:
            node = q.popleft()
            for child, sign in graph[node]:
                if child not in visited:
                    visited.add(child)
                    count += sign
                    q.append(child)
        
        return count