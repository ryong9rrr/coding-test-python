# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
접근 : DFS
시간복잡도 : 모든 노드의 개수를 N이라 할 때, O(N)
공간복잡도 : 리프 노드의 개수를 M이라 할 때, O(M)
"""
class Solution:
    def is_leaf(self, node):
        return node.left == None and node.right == None

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        def dfs(node, path):
            if self.is_leaf(node):
                result.append(path + str(node.val))
                return
            
            path += str(node.val)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, "")

        return sum(map(int, result))