# 동서남북으로 탐색 // 264ms
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i, j):
            # 범위를 벗어나거나 섬이 아니면
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "1":
                return
            # 마킹처리
            grid[i][j] = "0"
            # 동서남북으로 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    # 한 사이클이 끝났다면 섬을 하나 찾은 것
                    count += 1
                    
        return count