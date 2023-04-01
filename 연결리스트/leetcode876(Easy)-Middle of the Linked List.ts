/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

// 런너 기법
function middleNode(head: ListNode | null): ListNode | null {
  if (!head) {
    return null
  }

  let fast = head
  let slow = fast

  while (fast.next && fast.next.next) {
    slow = slow.next
    fast = fast.next.next
  }

  return fast.next ? slow.next : slow
}
