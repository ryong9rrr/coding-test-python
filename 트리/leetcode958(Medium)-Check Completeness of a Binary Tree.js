/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 접근 : DFS
// - 시간복잡도 : O(N)
// - 공간복잡도 : O(1)
const countNodes = (node) => {
  return node ? 1 + countNodes(node.left) + countNodes(node.right) : 0
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isCompleteTree = function (root) {
  const n = countNodes(root)

  const dfs = (node, index) => {
    if (!node) {
      return true
    }

    if (index >= n) {
      return false
    }

    return dfs(node.left, 2 * index + 1) && dfs(node.right, 2 * index + 2)
  }

  return dfs(root, 0)
}
