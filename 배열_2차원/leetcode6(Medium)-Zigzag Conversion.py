# 참고로 만약 이 문제가 코딩 인터뷰로 나온다면, 아래 풀이를 기대할 가능성이 크다.
# O(N)의 시간복잡도와 O(1)의 공간복잡도로 최적화한 풀이가 존재하는데, 이 풀이는 떠올리기가 어렵다.
# 최적화된 풀이는 리트코드 솔루션 2에서 제공하고 있다.

# 나의 풀이(리트코드 솔루션 1 - "구현" 풀이와 거의 동일) : 379ms(13.25%), 20.8MB(8.80%)
# 시간복잡도 : O(numRows * s의 길이)
class Solution:
    def fill_matrix(self, matrix, limit):
        n = len(matrix)
        dx = [1, -1]
        dy = [0, 1]
        
        x = y = 0
        direction = 0
        i = 0
        while i < limit:
            matrix[x][y] = i
            i += 1
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx == n - 1:
                direction = 1
            elif nx == 0:
                direction = 0
            x = nx
            y = ny


    def initialize_matrix(self, num_rows, limit):
        num_columns = math.ceil(limit / (2 * num_rows - 2)) * (num_rows - 1)
        return [[None] * num_columns for _ in range(num_rows)]


    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = self.initialize_matrix(numRows, len(s))
        self.fill_matrix(matrix, len(s))

        result = ""
        for row in matrix:
            for value in row:
                if value is not None:
                    result += s[value]

        return result