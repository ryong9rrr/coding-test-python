# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# stack을 이용한 일반적 풀이 // 28ms
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = deque()
        node = head
        
        while node:
            stack.append(node.val)
            node = node.next
            
        root = current = ListNode()
        
        while stack:
            current.next = ListNode(stack.pop())
            current = current.next
            
        return root.next


# 재귀 // 24ms
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(node, prev=None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)


# while문 // 24ms
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev