# 최단거리 경우의 수 문제와 비슷한 유형, 다만 여기서는 경우의 수가 아니라 거리마다 비용이 있기 때문에
# 단 하나의 최단거리가 존재하고, 그 최단거리의 비용을 구하는 문제. <최단거리 경우의 수> 문제와 기본적으로 원리는 같다.

# 행렬 최단거리 문제는 동적계획법으로 풀이한다 : 85ms(99.4%), 15.8MB(46.72%)
# 시간복잡도: O(N * M)
# 공간복잡도: O(1) - 여기서는 따로 DP행렬을 생성하지 않고 바로 원본 배열을 변형했기 때문.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j],  grid[i][j - 1])

        return grid[n - 1][m - 1]