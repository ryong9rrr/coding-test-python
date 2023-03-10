# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 해시 풀이 : 시간복잡도 O(n), 공간복잡도 O(n)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        
        return None
    
# 귀납적 접근 : 시간복잡도 O(n), 공간복잡도 O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                result = head
                while result != slow:
                    slow = slow.next
                    result = result.next
                return result

        return None