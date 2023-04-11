// 유니온파인드 : 193ms(94.29%), 73.5MB(94.29%)
const findParent = (parent, v) => {
  if (parent[v] !== v) {
    parent[v] = findParent(parent, parent[v])
  }
  return parent[v]
}

const unionParent = (parent, v, w) => {
  const x = findParent(parent, v)
  const y = findParent(parent, w)
  if (x < y) {
    parent[y] = x
  } else {
    parent[x] = y
  }
}

/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function (n, roads) {
  const parent = Array.from({ length: n + 1 }, (v, i) => i)
  roads.forEach(([v, w]) => unionParent(parent, v, w))

  let ans = Infinity
  const p = findParent(parent, 1)
  roads.forEach(([v, _, distance]) => {
    if (p === findParent(parent, v)) {
      ans = Math.min(ans, distance)
    }
  })

  return ans
}
