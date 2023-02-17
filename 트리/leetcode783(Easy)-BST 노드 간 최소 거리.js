/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 중위순회(재귀) : 64ms(78.82%), 42.1MB(96.47%)
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function (root) {
  let prev = -Infinity
  let result = Infinity

  const inOrder = (node) => {
    if (node.left) {
      inOrder(node.left)
    }

    result = Math.min(result, node.val - prev)
    prev = node.val

    if (node.right) {
      inOrder(node.right)
    }
  }

  inOrder(root)

  return result
}

// 중위순회(스택) : 66ms(71.18%), 43.1MB(62.35%)
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function (root) {
  let prev = -Infinity
  let result = Infinity

  let node = root
  const stack = []
  while (stack.length > 0 || node) {
    while (node) {
      stack.push(node)
      node = node.left
    }

    node = stack.pop()
    result = Math.min(result, node.val - prev)
    prev = node.val

    node = node.right
  }

  return result
}
