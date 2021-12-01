# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 분기를 이용한 일반적 풀이 // 24ms
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = current = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                v = l1.val
                l1 = l1.next
            else:
                v = l2.val
                l2 = l2.next
                    
            current.next = ListNode(v)
            current = current.next
        
        # 남아있는 원소들을 모두 넣어줍니다.
        while l1:
            current.next = ListNode(l1.val)
            current = current.next
            l1 = l1.next
            
        while l2:
            current.next = ListNode(l2.val)
            current = current.next
            l2 = l2.next
        
        return root.next
            
            
# 재귀 // 28ms ... 이해하기 어려운 코드
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
            
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
            
        return l1
        

# 좀 더 직관적인 재귀코드 // 28ms
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2