# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 런너기법으로 연결리스트를 모두 분할한 후 병합 // 650ms (20%)
class Solution(object):
    
    # 연결리스트를 병합하는 함수
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        
        # 런너기법으로 연결리스트를 반으로 분할
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.mergeTwoLists(l1, l2)