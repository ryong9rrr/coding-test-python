# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
접근 1 : 분할과 정복 + 리스트 슬라이싱
시간복잡도 : O(N^2), 148ms(51.92%)
공간복잡도 : O(N^2), 53.5MB(46.99%)
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(postorder.pop())

            node = TreeNode(inorder[index])
            node.right = self.buildTree(inorder[index + 1:], postorder)
            node.left = self.buildTree(inorder[:index], postorder)

            return node

        return None
    

"""
접근 2 : 분할과 정복 + 해시테이블로 최적화
시간복잡도 : O(N), 62ms(78.32%)
공간복잡도 : O(N), 18.9MB(74.9%)
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hash_map = {}
        for i, v in enumerate(inorder):
            hash_map[v] = i

        def recur(left, right):
            if left > right:
                return None
            
            node = TreeNode(postorder.pop())
            mid = hash_map[node.val]

            node.right = recur(mid + 1, right)
            node.left = recur(left, mid - 1)

            return node

        return recur(0, len(inorder) - 1)