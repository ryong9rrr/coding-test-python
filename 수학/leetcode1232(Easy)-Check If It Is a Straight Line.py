# 기울기 구하기
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        INF = int(1e9)
        def calculate_inc(a, b):
            x1, y1 = a
            x2, y2 = b
            dy = y1 - y2
            dx = x1 - x2
            if dy == 0:
                return INF
            if dx == 0:
                return -INF
            return dy / dx

        inc = calculate_inc(coordinates[0], coordinates[1])
        for i in range(len(coordinates) - 1):
            if inc != calculate_inc(coordinates[i], coordinates[i + 1]):
                return False
        return True