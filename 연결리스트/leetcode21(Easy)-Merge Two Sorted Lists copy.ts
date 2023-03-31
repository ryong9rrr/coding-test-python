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

// 1. 반복문 풀이
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  let current = new ListNode()
  const root = current

  while (list1 && list2) {
    let value = list1.val
    if (list1.val < list2.val) {
      list1 = list1.next
    } else {
      value = list2.val
      list2 = list2.next
    }

    current.next = new ListNode(value)
    current = current.next
  }

  while (list1) {
    current.next = new ListNode(list1.val)
    current = current.next
    list1 = list1.next
  }

  while (list2) {
    current.next = new ListNode(list2.val)
    current = current.next
    list2 = list2.next
  }

  return root.next
}

// 2. 재귀 풀이
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  if (list1 && list2) {
    if (list1.val > list2.val) {
      ;[list1, list2] = [list2, list1]
    }
    list1.next = mergeTwoLists(list1.next, list2)
  }
  return list1 || list2
}
