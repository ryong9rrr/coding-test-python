# dfs // 76ms (81.25%)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = collections.defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set()
        
        def dfs(node):
            # 순환구조라면
            if node in traced:
                return False
            # 순환구조는 아니지만 이미 방문했다면 더이상 볼필요 없음
            if node in visited:
                return True
            traced.add(node)
            for v in graph[node]:
                if not dfs(v):
                    return False
            traced.remove(node)
            visited.add(node)
            return True
            
        for node in graph.keys():
            if not dfs(node):
                return False
        return True