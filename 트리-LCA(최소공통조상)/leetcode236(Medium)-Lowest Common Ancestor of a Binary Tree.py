# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 접근 1 ) DFS : 64ms(93.10%), 26.3MB(56.42%)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root

        def dfs(node):
            nonlocal ans
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                ans = node
            return mid or left or right

        dfs(root)

        return ans
    

# 접근 2 ) 스택(큐도 가능) + 반복문 + 해시 : 68ms(84.59%), 18.5Mb(95.91%)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {
            root: None
        }

        while not (p in parent and q in parent):
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q