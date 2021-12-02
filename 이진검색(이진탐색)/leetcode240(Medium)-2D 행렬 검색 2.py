"""
맨 뒤의 값을 기준하여 target이 맨 뒤의 값보다 크면 row + 1, 작으면 col - 1
"""
# 132ms (92%)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        # 첫 행의 맨 뒤의 값: matrix[row][col]
        row, col = 0, len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
        return False
                

"""
파이썬다운 방식, 행렬에 값이 존재하는지 위에서부터 차례대로 탐색
"""
# 136ms
class Solution(object):
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)