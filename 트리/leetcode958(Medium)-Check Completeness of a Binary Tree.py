# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
접근 1 : BFS
- 시간복잡도 : 이진트리 모든 노드의 개수를 N이라 하고, 리프노드의 개수를 M이라 할 때 O(2 * N + 3 * M)
- 공간복잡도 : O(N + M)
"""
class Solution:
    def level_order(self, root: Optional[TreeNode]):
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()

                if not node:
                    result.append(None)
                    continue
                
                result.append(node)
                q.append(node.left)
                q.append(node.right)
               
        while result and result[-1] is None:
            result.pop()

        return result

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        levels = self.level_order(root)

        for i in range(len(levels) - 1):
            if levels[i] is None:
                return False

        return True
    

"""
접근 2 : DFS
- 시간복잡도 : 전체 노드의 개수를 N이라 하면 O(2 * N)
- 공간복잡도 : O(1)
"""
class Solution:
    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        n = self.count_nodes(root)

        def dfs(node, index):
            if not node:
                return True
            if index >= n:
                return False
            
            return dfs(node.left, 2 * index + 1) and dfs(node.right, 2 * index + 2)

        return dfs(root, 0)