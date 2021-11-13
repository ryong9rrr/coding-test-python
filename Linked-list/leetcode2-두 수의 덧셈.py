# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 정직한 풀이... // 68ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 재귀적으로 연결리스트를 뒤집는 함수
        def reverseLinkedList(node, prev=None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverseLinkedList(next, node)
        r1 = reverseLinkedList(l1)
        r2 = reverseLinkedList(l2)
        
        # 연결리스트를 리스트로 만드는 함수
        def toListFromLinkedList(node, arr):
            while node:
                arr.append(node.val)
                node = node.next
            return arr
        
        list1 = []
        toListFromLinkedList(r1, list1)
        list2 = []
        toListFromLinkedList(r2, list2)
        
        # 합을 구함
        total = int("".join([str(x) for x in list1])) + int("".join([str(x) for x in list2]))
        total = list(str(total))
        
        stack = deque()
        for i in total:
            stack.append(i)
        
        # 정답 도출
        root = current = ListNode()
        while stack:
            current.next = ListNode(stack.pop())
            current = current.next
        return root.next

# 정직한 풀이2... // 72ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = deque()
        stack2 = deque()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        s1 = ""
        s2 = ""
        while stack1:
            s1 += str(stack1.pop())
        while stack2:
            s2 += str(stack2.pop())

        total = list(str(int(s1) + int(s2)))[::-1]
        root = current = ListNode()
        for s in total:
            current.next = ListNode(int(s))
            current = current.next
        return root.next

# 우아한 풀이) 전가산기 구현 // 68ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 전가산기 구현
        root = head = ListNode()
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next        
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next