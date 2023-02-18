/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 재귀 : 72ms(35.73%), 42.2MB(58.73%)
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (!root) {
    return null
  }

  const left = invertTree(root.right)
  const right = invertTree(root.left)
  root.left = left
  root.right = right
  return root
}

// 스택 : 68ms(53.21%), 42.4MB(35.99%)
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  const stack = [root]

  while (stack.length > 0) {
    const node = stack.pop()
    if (node) {
      const temp = node.right
      node.right = node.left
      node.left = temp
      stack.push(node.left)
      stack.push(node.right)
    }
  }

  return root
}
