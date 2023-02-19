// BFS : 68ms(70.47%), 43.6MB(84.58%)
class MyNode {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class MyQueue {
  constructor() {
    this.front = this.tail = null
    this.size = 0
  }

  get peek() {
    return !this.front || !this.tail ? undefined : this.front.value
  }

  get desc() {
    const result = []
    let node = this.front
    while (node) {
      result.push(node.value)
      node = node.next
    }
    return result.join(" ")
  }

  enqueue(value) {
    const node = new MyNode(value)
    if (!this.front) {
      this.front = this.tail = node
    } else {
      this.tail = this.tail.next = node
    }
    this.size += 1
  }

  dequeue() {
    if (!this.front) {
      return undefined
    }
    const result = this.front.value
    this.front = this.front.next
    this.size -= 1
    return result
  }
}

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function (root) {
  if (!root) {
    return []
  }

  const levels = []
  const q = new MyQueue()
  q.enqueue(root)

  while (q.size > 0) {
    const n = q.size
    const level = []
    for (let i = 0; i < n; i += 1) {
      const node = q.dequeue()
      if (node) {
        level.push(node.val)

        if (node.left) {
          q.enqueue(node.left)
        }

        if (node.right) {
          q.enqueue(node.right)
        }
      }
    }

    levels.push(level)
  }

  return levels.map((level, i) => {
    if (i % 2 === 1) {
      return level.reverse()
    }
    return level
  })
}
