# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 재귀구조 DFS로 모든 노드를 완전탐색 // 344ms (25%)
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)
        return (root.val if low <= root.val <= high else 0) + left + right


# 2. 분기를 통한 가지치기로 DFS 최적화 // 250ms (75%)
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

# 2-1. 반복구조 DFS(스택), BFS(큐)
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        stack, total = deque([root]), 0
        
        while stack:
            # 큐라면 popleft()
            node = stack.pop()
            
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    total += node.val
        
        return total