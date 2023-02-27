// DFS : 78ms(82.40%), 50.8MB(97.72%)
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  let ans = root

  const dfs = (node) => {
    if (!node) {
      return false
    }

    const left = dfs(node.left)
    const right = dfs(node.right)
    const mid = node === p || node === q

    if (mid + left + right >= 2) {
      ans = node
    }
    return mid || left || right
  }

  dfs(root)

  return ans
}

// 자바스크립트의 딕셔너리 key는 문자열이라서 key에 바로 노드를 저장할 수 없다. 그래서 따로 `nodes` 라는 테이블을 생성함.
// 88ms(44.20%), 50.9MB(96.27%)
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  const parent = {
    [root.val]: null,
  }

  const nodes = {}

  const stack = [root]

  let x = p.val
  let y = q.val

  while (stack.length > 0 && !(x in parent && y in parent)) {
    const node = stack.pop()
    nodes[node.val] = node

    if (!node) {
      continue
    }

    if (node.left) {
      parent[node.left.val] = node.val
      stack.push(node.left)
    }

    if (node.right) {
      parent[node.right.val] = node.val
      stack.push(node.right)
    }
  }

  const ancestors = new Set()
  while (x !== null) {
    ancestors.add(x)
    x = parent[x]
  }

  while (!ancestors.has(y)) {
    y = parent[y]
  }

  return nodes[y]
}
