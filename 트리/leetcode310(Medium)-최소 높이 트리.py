# 200ms (80%)
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        
        graph = defaultdict(list)
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves
                    