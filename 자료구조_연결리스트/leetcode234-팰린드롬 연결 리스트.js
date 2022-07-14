/**
 * 1677ms, 5%
 * shift 메서드 사용
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
var isPalindrome = function (head) {
  const q = []

  if (!head) return true

  let node = head

  while (node) {
    q.push(node.val)
    node = node.next
  }

  while (q.length > 1) {
    if (q.shift() !== q.pop()) return false
  }
  return true
}
