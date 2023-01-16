// 반복문 중위순회: 71ms, 45.7MB
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  const result = []

  const stack = []
  while (stack.length > 0 || root) {
    while (root) {
      stack.push(root)
      root = root.left
    }
    root = stack.pop()
    if (result.length > 0 && result[result.length - 1] >= root.val) {
      return false
    }
    result.push(root.val)
    root = root.right
  }

  return true
}
