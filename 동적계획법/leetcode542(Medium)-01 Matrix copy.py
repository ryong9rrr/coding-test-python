# 접근 1 : BFS, 710ms(58.26%), 17.4MB(41.48%)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        N = len(mat)
        M = len(mat[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def validate_range(nx, ny):
            return 0 <= nx < N and 0 <= ny < M

        visited = [[-1] * M for _ in range(N)]
        q = collections.deque()
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    visited[i][j] = 0
                    q.append((i, j, 0))

        while q:
            x, y, dist = q.popleft()
            ndist = dist + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if validate_range(nx, ny) and visited[nx][ny] == -1:
                    visited[nx][ny] = ndist
                    q.append((nx, ny, ndist))

        return visited
    
# 접근 2 : DP, 564ms(91.54%), 17.1MB(55.67%)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        N = len(mat)
        M = len(mat[0])
        MAX_DISTANCE = N * M + 1
        dp = [[MAX_DISTANCE] * M for _ in range(N)]

        # top-left => bottom-right
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    continue
                top = left = MAX_DISTANCE
                if i > 0:
                    top = dp[i - 1][j] + 1
                if j > 0:
                    left = dp[i][j - 1] + 1
                dp[i][j] = min(dp[i][j], top, left)

        # bottom-right => top-left
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                bottom = right = MAX_DISTANCE
                if i < N - 1:
                    bottom = dp[i + 1][j] + 1
                if j < M - 1:
                    right = dp[i][j + 1] + 1
                dp[i][j] = min(dp[i][j], bottom, right)

        return dp