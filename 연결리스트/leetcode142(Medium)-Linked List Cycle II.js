/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

// 해시 풀이 : 시간복잡도 O(n), 공간복잡도 O(n)
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  const visited = new Set()
  let node = head

  while (node) {
    if (visited.has(node)) {
      return node
    }
    visited.add(node)
    node = node.next
  }

  return null
}

// 귀납적 접근 : 시간복잡도 O(n), 공간복잡도 O(1)
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  if (!head) {
    return null
  }

  let slow = head
  let fast = head

  while (fast.next && fast.next.next) {
    slow = slow.next
    fast = fast.next.next

    if (slow === fast) {
      let result = head
      while (slow !== result) {
        slow = slow.next
        result = result.next
      }
      return result
    }
  }

  return null
}
