# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 재귀로 분할정복 // 124ms (65%)
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])
            
            return node