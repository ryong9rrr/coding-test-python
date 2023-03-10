# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Reservoir sampling (저수지 샘플링) 알고리즘 : 시간복잡도 O(n), 공간복잡도 O(1)
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = None
        i = 1

        node = self.head
        while node:
            if random.random() < (1 / i): # Reservoir sampling
                result = node.val
            node = node.next
            i += 1
        return result