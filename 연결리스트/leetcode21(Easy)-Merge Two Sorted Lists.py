# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 메모리를 생성하여 일반적인 분기풀이
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = current = ListNode()

        while list1 and list2:
            value = list1.val
            if list1.val < list2.val:
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            
            current.next = ListNode(value)
            current = current.next

        while list1:
            current.next = ListNode(list1.val)
            current = current.next
            list1 = list1.next

        while list2:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next

        return root.next
    

# 재귀...
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2