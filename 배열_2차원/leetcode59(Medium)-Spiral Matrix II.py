# 32ms, 14.2MB
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        matrix = [[0] * n for _ in range(n)]
        
        def fill_matrix(x, y, number, direction):
            if number > n ** 2:
                return
            matrix[x][y] = number
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] > 0:
                direction = (direction + 1) % 4
            fill_matrix(x + dx[direction], y + dy[direction], number + 1, direction)
            
            
        fill_matrix(0, 0, 1, 0)
        
        return matrix