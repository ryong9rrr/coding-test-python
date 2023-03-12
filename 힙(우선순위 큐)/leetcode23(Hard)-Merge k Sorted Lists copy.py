# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
접근 1 : 정렬을 사용한 풀이
- 시간복잡도 O(N * logN) : k개 연결리스트의 모든 노드의 개수를 N이라고 할 때, 
모든 노드를 한 번 순회하고 그만큼 정렬하는 시간이 필요하므로
- 공간복잡도 O(N) : k개 연결리스트의 모든 노드의 개수를 저장해야하므로
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numbers = []
        for head in lists:
            node = head
            while node:
                numbers.append(node.val)
                node = node.next

        numbers.sort()

        head = None
        while numbers:
            number = numbers.pop()
            node = ListNode(number)
            node.next = head
            head = node
        
        return head


"""
접근 2 : 우선순위 큐(힙)
- 시간복잡도 : N개의 노드를 heapify 하므로 O(N * logN)
- 공간복잡도 : N개의 노드를 저장하므로 O(N)

이 문제는 <파이썬 알고리즘 인터뷰> 에도 나온 문제임 (우선순위 큐 - k개 정렬리스트의 병합)
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode(None)
        heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        head = root
        while heap:
            _, i, node = heapq.heappop(heap)
            
            head.next = node
            head = head.next

            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return root.next
    

"""
접근 3 : 재귀적으로 병합
- 시간복잡도 : O(N * logN)
- 공간복잡도 : O(1)

아래 'mergeTwoLists()' 함수는 <파이썬 알고리즘 인터뷰 - 연결리스트 - 두 정렬리스트의 병합> 문제에 나온 코드임.
"""
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        interval = 1
        
        if n == 0:
            return None

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]