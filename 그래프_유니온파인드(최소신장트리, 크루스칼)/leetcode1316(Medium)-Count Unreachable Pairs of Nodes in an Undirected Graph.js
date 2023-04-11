// 접근 : 유니온파인드 + 수학(약간의 수학적 규칙)
// - 시간복잡도 : 노드의 개수가 N, 간선의 개수가 E 일 때 O(N + E)
// - 공간복잡도 : O(N)
const findParent = (parent, x) => {
  if (parent[x] !== x) {
    parent[x] = findParent(parent, parent[x])
  }
  return parent[x]
}

const unionParent = (parent, a, b) => {
  const x = findParent(parent, a)
  const y = findParent(parent, b)
  if (x === y) {
    return
  }
  if (x < y) {
    parent[y] = x
  } else {
    parent[x] = y
  }
}

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countPairs = function (n, edges) {
  const parent = Array.from({ length: n }, (v, i) => i)
  edges.forEach(([v, w]) => unionParent(parent, v, w))

  const groups = parent
    .map((v) => findParent(parent, v))
    .reduce((obj, v) => {
      if (!obj[v]) obj[v] = 0
      obj[v] += 1
      return obj
    }, {})

  return Object.values(groups).reduce((ans, count) => {
    ans += count * (n - count)
    n -= count
    return ans
  }, 0)
}
