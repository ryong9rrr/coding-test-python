# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 재귀로 중위순회 : 35ms, 17MB
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = True
        stack = []
        def inorder(node):
            nonlocal result
            if node is None or not result:
                return
            inorder(node.left)
            if stack and stack[-1] >= node.val:
                result = False
            stack.append(node.val)
            inorder(node.right)
        inorder(root)

        return result
    
# 반복문으로 중위순회 : 38ms, 16.4MB
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if result and result[-1] >= root.val:
                return False
            result.append(root.val)
            root = root.right

        return True