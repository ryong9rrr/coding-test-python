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

// 스택을 이용한 일반적 풀이
function reverseList(head: ListNode | null): ListNode | null {
  const stack: number[] = []
  while (head) {
    stack.push(head.val)
    head = head.next
  }

  let current = new ListNode()
  const root = current

  while (stack.length > 0) {
    const v = stack.pop()
    current.next = new ListNode(v)
    current = current.next
  }

  return root.next
}

// 재귀
const reverse = (node: ListNode | null, prev: ListNode | null = null) => {
  if (!node) {
    return prev
  }
  const nextNode = node.next
  node.next = prev
  return reverse(nextNode, node)
}

function reverseList(head: ListNode | null): ListNode | null {
  return reverse(head)
}

// while 문
function reverseList(head: ListNode | null): ListNode | null {
  let node: ListNode | null = head
  let prev: ListNode | null = null

  while (node) {
    const nextNode = node.next
    node.next = prev

    prev = node
    node = nextNode
  }

  return prev
}
