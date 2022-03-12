# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# deque 사용 // 1112ms
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = deque()
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True

"""js 
1677ms, 5%
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    const q = [];
    
    if (!head) return true
    
    let node = head
    
    while (node){
        q.push(node.val)
        node = node.next
    }
    
    while (q.length > 1){
        if (q.shift() !== q.pop()) return false
    }
    return true
    
};
"""


# 런너(runner)기법 // 816ms
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            # 꼭 다중할당을 해야함
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev

#Best solution
def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

"""js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let fast;
    let slow;
    fast = slow = head;
    
    while (fast && fast.next){
        fast = fast.next.next;
        slow = slow.next;
    }
    
    let node = null;
    while (slow){
        next = slow.next;
        slow.next = node;
        node = slow;
        slow = next;
    }
    
    while (node){
        if (node.val !== head.val) return false;
        node = node.next;
        head = head.next;
    }
    return true
};
"""