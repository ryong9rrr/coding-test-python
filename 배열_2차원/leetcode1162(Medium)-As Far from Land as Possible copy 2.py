# 접근 1 : BFS, 723ms(45.57%), 14.5MB(80.10%)
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def validate_range(nx, ny):
            return 0 <= nx < N and 0 <= ny < N

        lands_q = collections.deque()
        visited = [[-1] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    lands_q.append((i, j, 0))
                    visited[i][j] = 0

        while lands_q:
            x, y, dist = lands_q.popleft()
            ndist = dist + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if validate_range(nx, ny) and visited[nx][ny] == -1:
                    visited[nx][ny] = ndist
                    lands_q.append((nx, ny, ndist))

        result = 0
        for i in range(N):
            for j in range(N):
                result = max(result, visited[i][j])

        return result if result > 0 else -1
    
# 접근 2 : DP, 516ms(92.69%), 14.2MB(99.16%)
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        MAX_DISTANCE = N * 2 + 1
        dp = [[MAX_DISTANCE] * N for _ in range(N)]

        # update top, left => bottom, right direction
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                top_dist = MAX_DISTANCE
                if i > 0:
                    top_dist = dp[i - 1][j] + 1
                left_dist = MAX_DISTANCE
                if j > 0:
                    left_dist = dp[i][j - 1] + 1
                dp[i][j] = min(dp[i][j], top_dist, left_dist)

        # update bottom, right => top, left direction
        ans = 0
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                bottom_dist = MAX_DISTANCE
                if i < N - 1:
                    bottom_dist = dp[i + 1][j] + 1
                right_dist = MAX_DISTANCE
                if j < N - 1:
                    right_dist = dp[i][j + 1] + 1
                dp[i][j] = min(dp[i][j], right_dist, bottom_dist)
                ans = max(ans, dp[i][j])

        if ans == 0 or ans == MAX_DISTANCE:
            return -1
        return ans