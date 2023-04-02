"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 접근 : DFS
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            for next_node in node.children:
                dfs(next_node)

        dfs(root)

        return ans