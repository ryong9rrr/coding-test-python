/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 접근 1 : 분할과 정복 + 리스트 슬라이싱
// 시간복잡도 : O(N^2), 167ms(16.37%)
// 공간복잡도 : O(N^2), 82.2MB(43.64%)
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function (inorder, postorder) {
  if (inorder.length > 0) {
    const x = postorder.pop()
    const index = inorder.findIndex((v) => v === x)

    const node = new TreeNode(inorder[index])
    node.right = buildTree(inorder.slice(index + 1), postorder)
    node.left = buildTree(inorder.slice(0, index), postorder)

    return node
  }

  return null
}

// 접근 2 : 분할과 정복 + 해시테이블로 최적화
// 시간복잡도: O(N), 64ms(99.55%)
// 공간복잡도 : O(N), 44.5MB(85%)
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function (inorder, postorder) {
  const hashMap = new Map()
  inorder.forEach((v, i) => {
    hashMap.set(v, i)
  })

  const recur = (left, right) => {
    if (left > right) {
      return null
    }

    const node = new TreeNode(postorder.pop())
    const mid = hashMap.get(node.val)

    node.right = recur(mid + 1, right)
    node.left = recur(left, mid - 1)

    return node
  }

  return recur(0, inorder.length - 1)
}
