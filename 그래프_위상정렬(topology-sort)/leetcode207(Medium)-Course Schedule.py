"""
이 문제는 <파이썬 알고리즘 인터뷰>에 나와있는 문제로,
책에서는 dfs 풀이로 나와있다. 하지만 이 문제는 매우 전형적인 위상정렬 문제.
"""

# 위상정렬 풀이 : 93ms, 15.4MB
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = collections.defaultdict(list)
        for v, w in prerequisites:
            graph[v].append(w)
            indegree[w] += 1
        
        q = collections.deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)

        count = 0
        while q:
            count += 1
            v = q.popleft()
            for w in graph[v]:
                indegree[w] -= 1
                if indegree[w] == 0:
                    q.append(w)
                
        
        return count == numCourses
    
# dfs : 92ms, 17.5MB
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for v, w in prerequisites:
            graph[v].append(w)

        traced = set()
        visited = set()

        def dfs(v):
            if v in traced:
                return False
            if v in visited:
                return True
            
            traced.add(v)
            for w in graph[v]:
                if not dfs(w):
                    return False
            traced.remove(v)
            visited.add(v)
            return True


        for v in range(numCourses):
            if not dfs(v):
                return False
        
        return True