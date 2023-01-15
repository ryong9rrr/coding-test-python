# BFS : 53ms, 13.9MB
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        def validate_range(nx, ny):
            return 0 <= nx < N and 0 <= ny < M
        
        entire_count = 0
        rottens = collections.deque()
        for x in range(N):
            for y in range(M):
                if grid[x][y] != 0:
                    entire_count += 1
                    if grid[x][y] == 2:
                        rottens.append((x, y, 0))
        
        rotten_count = len(rottens)
        
        result = 0
        while rottens:
            x, y, time = rottens.popleft()
            result = max(result, time)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if validate_range(nx, ny) and grid[nx][ny] == 1:
                    rotten_count += 1
                    grid[nx][ny] = 2
                    rottens.append((nx, ny, time + 1))
            
            
        if entire_count - rotten_count > 0 :
            return -1
        return result