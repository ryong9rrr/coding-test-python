# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 최적화 전 // 1800ms
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = parent = ListNode(None)
        
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            cur = parent
            
        return parent.next

# 최적화 // 148ms
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = parent = ListNode(None)
        
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            # 값이 클 때만 포인터를 처음으로 돌려보낸다.
            if head and cur.val > head.val:
                cur = parent
            
        return parent.next