# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS + 백트래킹 : 53ms(70.76%), 24.5MB(23.66%)
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        visited = {}
        result = set()

        def dfs(node):
            if not node:
                return "()"

            left = dfs(node.left)
            right = dfs(node.right)

            representation = "(" + left + str(node.val) + right + ")"

            if representation in visited:
                result.add(representation)
            else:
                visited[representation] = node
            
            return representation

        dfs(root)

        return [visited[representation] for representation in list(result)]