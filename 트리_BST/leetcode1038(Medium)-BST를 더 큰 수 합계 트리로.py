# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 중위순회하며 total값을 노드에 저장
class Solution(object):
    
    total = 0
    
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.bstToGst(root.right)
            self.total += root.val
            root.val = self.total
            self.bstToGst(root.left)
        return root