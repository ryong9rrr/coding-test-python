# 간단한 O(N) 순회문제
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def valid(px, py):
            return x == px or y == py

        def mht(px, py):
            return abs(x - px) + abs(y - py)

        min_dist = int(1e9)
        valid_points = []
        for index, coor in enumerate(points):
            px, py = coor
            if not valid(px, py):
                continue
            dist = mht(px, py)
            valid_points.append([index, dist])
            min_dist = min(min_dist, dist)

        for index, dist in valid_points:
            if dist == min_dist:
                return index
        
        return -1