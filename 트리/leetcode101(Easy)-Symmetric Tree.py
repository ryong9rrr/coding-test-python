# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
접근 1 : 트리 순회
- 시간복잡도 : 트리의 전체 노드 개수가 N일 때, 4N = O(N)
- 공간복잡도 : 2 * N = O(N)
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pres = []
        posts = []

        def pre_order(node):
            if not node:
                pres.append("#")
                return
            pres.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)

        def post_order(node):
            if not node:
                posts.append("#")
                return
            post_order(node.left)
            post_order(node.right)
            posts.append(str(node.val))

        pre_order(root)
        post_order(root)

        return "".join(pres) == "".join(posts[::-1])
    
"""
접근 2 : 재귀 (최적화)
- 시간복잡도 : O(N)
- 공간복잡도 : O(1)
"""
class Solution:
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left or not right:
            return left == right

        if left.val != right.val:
            return False

        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.isMirror(root.left, root.right)