# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 스택을 이용한 일반적 풀이
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        root = current = ListNode()
        while stack:
            v = stack.pop()
            current.next = ListNode(v)
            current = current.next
        
        return root.next
    
    

# 재귀
class Solution:
    def reverse(self, node, prev = None):
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return self.reverse(next_node, node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)



# while 문
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next_node = node.next
            node.next = prev
            
            prev = node
            node = next_node
        
        return prev