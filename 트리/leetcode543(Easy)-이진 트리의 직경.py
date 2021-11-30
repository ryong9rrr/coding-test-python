# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs // 61ms, 15.00%
class Solution(object):
    
    longest = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest