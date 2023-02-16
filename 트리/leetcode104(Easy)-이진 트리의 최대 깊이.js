/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// BFS : 78ms(39.60%), 45.6MB(14.39%)
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
 * @return {number}
 */
var maxDepth = function (root) {
  if (root === null) {
    return 0
  }

  const q = new MyQueue()
  q.enqueue(root)

  let depth = 0
  while (q.size > 0) {
    depth += 1
    const n = q.size
    for (let i = 0; i < n; i += 1) {
      const node = q.dequeue()
      if (node.left !== null) {
        q.enqueue(node.left)
      }
      if (node.right !== null) {
        q.enqueue(node.right)
      }
    }
  }

  return depth
}

// DFS : 64ms(92.45%), 44.7MB(55.48%)
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  const dfs = (node, depth) => {
    if (node === null) {
      return depth
    }
    const leftDepth = dfs(node.left, depth + 1)
    const rightDepth = dfs(node.right, depth + 1)

    return Math.max(leftDepth, rightDepth)
  }

  return dfs(root, 0)
}
