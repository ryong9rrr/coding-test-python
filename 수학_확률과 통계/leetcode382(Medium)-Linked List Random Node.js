/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function (head) {
  this.head = head
}

/**
 * @return {number}
 */
Solution.prototype.getRandom = function () {
  let result = null
  let i = 1

  let node = this.head
  while (node) {
    if (Math.random() < 1 / i) {
      result = node.val
    }
    node = node.next
    i += 1
  }
  return result
}
