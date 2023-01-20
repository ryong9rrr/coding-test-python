# BFS : 36ms(98%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        q = collections.deque([(root, 0)])
        while q:
            last_idx = q[-1][1]
            first_idx = q[0][1]
            result = max(result, last_idx - first_idx + 1)
            
            for _ in range(len(q)):
                node, idx = q.popleft()
                sub_idx = idx - first_idx
                if node.left:
                    q.append((node.left, sub_idx * 2 + 1))
                if node.right:
                    q.append((node.right, sub_idx * 2 + 2))
        
        return result