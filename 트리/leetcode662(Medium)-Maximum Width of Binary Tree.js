// BFS : 82ms(77.40%)
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
var widthOfBinaryTree = function (root) {
  if (!root) {
    return 0
  }

  let result = 0
  const q = [[root, 0]]

  while (q.length > 0) {
    const lastIdx = q[q.length - 1][1]
    const firstIdx = q[0][1]

    result = Math.max(result, lastIdx - firstIdx + 1)

    let len = q.length
    while (len--) {
      const [node, idx] = q.shift()
      const subIdx = idx - firstIdx
      if (node.left) q.push([node.left, subIdx * 2 + 1])
      if (node.right) q.push([node.right, subIdx * 2 + 2])
    }
  }

  return result
}
