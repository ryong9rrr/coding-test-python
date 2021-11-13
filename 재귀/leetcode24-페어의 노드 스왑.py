# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 모든 노드를 순회하며 새로만든 리스트에 넣기 // 20ms
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = current = ListNode()
        
        while head and head.next:
            a, b = head.val, head.next.val
            current.next = ListNode(b)
            current.next.next = ListNode(a)
            current = current.next.next
            head = head.next.next
            
        while head:
            current.next = ListNode(head.val)
            current = current.next
            head = head.next
            
        return root.next

# 단순 swap(변칙적인 풀이 이므로 온라인코딩테스트에만 사용하자) // 16ms
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head

# 반복구조로 swap // 16ms
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        root = prev = ListNode()
        # 원소가 1개일 때를 위해
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
            
        return root.next
            

# 재귀로 스왑 // 12ms
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
            