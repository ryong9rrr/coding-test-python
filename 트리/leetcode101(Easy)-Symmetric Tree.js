/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 재귀
const isMirror = (left, right) => {
  if (!left || !right) {
    return left === right
  }

  if (left.val !== right.val) {
    return false
  }

  return isMirror(left.left, right.right) && isMirror(left.right, right.left)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  return !root || isMirror(root.left, root.right)
}
