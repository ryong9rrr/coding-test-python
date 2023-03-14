/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 접근 : DFS
// 시간복잡도 : 모든 노드의 개수를 N이라 할 때, O(N)
// 공간복잡도 : 여기서는 배열로 관리하지 않고 바로 result(정수형)에 더해주고 있으므로 O(1)
const isLeaf = (node) => {
  return node && node.left === null && node.right === null
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumNumbers = function (root) {
  if (!root) {
    return 0
  }

  let result = 0
  const dfs = (node, path) => {
    if (isLeaf(node)) {
      result += parseInt(path + String(node.val), 10)
      return
    }

    path += String(node.val)
    if (node.left) {
      dfs(node.left, path)
    }

    if (node.right) {
      dfs(node.right, path)
    }
  }

  dfs(root, "")

  return result
}
