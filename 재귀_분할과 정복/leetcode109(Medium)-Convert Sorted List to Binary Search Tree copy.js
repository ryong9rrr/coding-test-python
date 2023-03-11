/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 접근 1 : 분할과 정복 풀이
// - 시간복잡도 : 모든 연결리스트를 일단 한번 순회해야하기 때문에 연결리스트의 길이를 N이라고 할 때, O(N * logN)
// - 공간복잡도 : 모든 연결리스트의 val을 배열로 만들기 때문에 연결리스트의 길이를 N이라고 할 때, O(N)
const createBST = (left, right, values) => {
  if (left > right) {
    return null
  }

  const mid = left + Math.floor((right - left) / 2)
  const node = new TreeNode(values[mid])
  node.left = createBST(left, mid - 1, values)
  node.right = createBST(mid + 1, right, values)
  return node
}

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function (head) {
  const values = []
  while (head) {
    values.push(head.val)
    head = head.next
  }

  return createBST(0, values.length - 1, values)
}

// 접근 2 : 분할정복 + 런너 기법
// - 시간복잡도 : 매번 연결리스트를 절반씩 순회하는데, 결국 노드의 개수만큼 순회하는 것이므로 O(N)
// - 공간복잡도 : O(1)
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function (head) {
  if (!head) {
    return null
  }

  if (!head.next) {
    return new TreeNode(head.val)
  }

  let prev = null
  let slow = head
  let fast = head
  while (fast && fast.next) {
    prev = slow
    slow = slow.next
    fast = fast.next.next
  }

  prev.next = null

  const node = new TreeNode(slow.val)
  node.left = sortedListToBST(head)
  node.right = sortedListToBST(slow.next)

  return node
}
