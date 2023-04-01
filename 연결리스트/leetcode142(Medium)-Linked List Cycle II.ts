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

// 런너 풀이
function detectCycle(head: ListNode | null): ListNode | null {
  if (!head) {
    return null
  }

  let fast = head
  let slow = fast

  while (fast.next && fast.next.next) {
    slow = slow.next
    fast = fast.next.next

    if (slow === fast) {
      let result = head
      while (result !== slow) {
        result = result.next
        slow = slow.next
      }
      return result
    }
  }

  return null
}
