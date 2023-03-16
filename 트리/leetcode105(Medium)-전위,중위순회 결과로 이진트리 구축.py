# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
접근 1 : 분할과 정복 + 리스트 슬라이싱
시간복잡도 : O(N^2), 144ms(68.43%)
공간복잡도 : O(N^2), 53.5MB(55.57%)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])
            return node

        return None
    
"""
접근 2 : 분할과 정복 + 해시 + 큐로 최적화
시간복잡도 : O(N), 50ms(98.38%)
공간복잡도 : O(N), 18.8MB(86.74%)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_q = collections.deque(preorder)

        hash_map = {}
        for i, v in enumerate(inorder):
            hash_map[v] = i

        def recur(left, right):
            if left > right:
                return None

            node = TreeNode(preorder_q.popleft())
            mid = hash_map[node.val]
            
            node.left = recur(left, mid - 1)
            node.right = recur(mid + 1, right)

            return node

        return recur(0, len(inorder) - 1)