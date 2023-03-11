# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
접근 1 : 분할과 정복 풀이
- 시간복잡도 : 모든 연결리스트를 일단 한번 순회해야하기 때문에 연결리스트의 길이를 N이라고 할 때, O(N * logN)
- 공간복잡도 : 모든 연결리스트의 val을 배열로 만들기 때문에 연결리스트의 길이를 N이라고 할 때, O(N)
"""
class Solution:
    def createBST(self, left, right, values):
        if left > right:
            return None
        mid = left + ((right - left) // 2)
        node = TreeNode(values[mid])
        node.left = self.createBST(left, mid - 1, values)
        node.right = self.createBST(mid + 1, right, values)
        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        return self.createBST(0, len(values) - 1, values)
    

"""
접근 2 : 분할정복 + 런너 기법
- 시간복잡도 : 매번 연결리스트를 절반씩 순회하는데, 결국 노드의 개수만큼 순회하는 것이므로 O(N)
- 공간복잡도 : O(1)
"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:      
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)
        
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node