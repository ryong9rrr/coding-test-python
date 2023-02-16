# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS : 36ms(94.60%), 15.2MB(98.15%)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        q = collections.deque([root])
        depth = 0

        while q:
            depth += 1
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
    
# DFS : 46ms(54.48%), 16.4MB(18.14%)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return depth

            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            return max(left_depth, right_depth)

        return dfs(root, 0)