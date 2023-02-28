/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// DFS + 백트래킹 : 97ms(90.68%), 58.4MB(27.97%)
/**
 * @param {TreeNode} root
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function (root) {
  const visited = {}
  const result = new Set()

  const dfs = (node) => {
    if (!node) {
      return "()"
    }

    const left = dfs(node.left)
    const right = dfs(node.right)

    const representation = `(${left}${node.val}${right})`

    if (representation in visited) {
      result.add(representation)
    } else {
      visited[representation] = node
    }

    return representation
  }

  dfs(root)

  return Array.from(result).map((representation) => visited[representation])
}
