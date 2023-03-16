/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// 접근 1 : 분할과 정복 + 리스트 슬라이싱
// 시간복잡도 : O(N^2), 129ms(55.16%)
// 공간복잡도 : O(N^2), 82MB(56.51%)
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  if (inorder.length > 0) {
    const x = preorder.shift()
    const index = inorder.findIndex((v) => v === x)

    const node = new TreeNode(inorder[index])
    node.left = buildTree(preorder, inorder.slice(0, index))
    node.right = buildTree(preorder, inorder.slice(index + 1))

    return node
  }

  return null
}

// 접근 2 : 분할과 정복 + 해시로 최적화
// (node의 개수가 최대 3000이기 때문에 큐 모듈을 사용하지 않았음, 사용해도 시간차이 없었음.)
// 시간복잡도 : O(N), 78ms(89%)
// 공간복잡도 : O(N), 45.1MB(76.57%)
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  const hashMap = new Map()
  inorder.forEach((v, i) => {
    hashMap.set(v, i)
  })

  const recur = (left, right) => {
    if (left > right) {
      return null
    }

    const node = new TreeNode(preorder.shift())
    const mid = hashMap.get(node.val)

    node.left = recur(left, mid - 1)
    node.right = recur(mid + 1, right)

    return node
  }

  return recur(0, inorder.length - 1)
}
