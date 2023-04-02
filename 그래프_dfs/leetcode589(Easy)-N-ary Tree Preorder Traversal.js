/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

// DFS
/**
 * @param {Node|null} root
 * @return {number[]}
 */
var preorder = function (root) {
  const ans = []

  const dfs = (node) => {
    if (!node) return
    ans.push(node.val)
    for (const nextNode of node.children) {
      dfs(nextNode)
    }
  }

  dfs(root)

  return ans
}
