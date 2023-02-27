# 124ms(49.86%), 14.7MB(86.50%)
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def divide(self, n: int, i: int, j: int, grid: List[List[int]]) -> Node:
        # (2) 1x1 원소가 되면 리프노드인 것이므로 노드를 생성해서 반환
        if n <= 1:
            return Node(grid[i][j], 1, None, None, None, None)
        
        # (1) 일단 나눌 수 있을때까지(1x1 원소가 될 때까지) 나눔
        mid = n // 2
        top_left = self.divide(mid, i, j, grid)
        top_right = self.divide(mid, i, j + mid, grid)
        bottom_left = self.divide(mid, i + mid, j, grid)
        bottom_right = self.divide(mid, i + mid, j + mid, grid)

        # (3-1) 4분할된 노드가 모두 리프노드이고 값이 같다면 하나의 노드로 다시 만들어서 반환
        if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and \
            top_left.val == top_right.val == bottom_left.val == bottom_right.val:
            return Node(top_left.val, 1, None, None, None, None)

        # (3-2) 그렇지 않다면 리프노드가 아니라는 처리(2번째 인자) 4분할된 하위 노드를 그대로 넘겨줌
        return Node(grid[i][j], 0, top_left, top_right, bottom_left, bottom_right)

    def construct(self, grid: List[List[int]]) -> Node:
        return self.divide(len(grid), 0, 0, grid)
        