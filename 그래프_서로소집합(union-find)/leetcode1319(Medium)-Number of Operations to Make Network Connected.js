// 유니온파인드 풀이 : 102ms(94.74%), 55.2MB(89.47%)

const findParent = (parent, x) => {
  if (parent[x] !== x) {
    parent[x] = findParent(parent, parent[x])
  }
  return parent[x]
}

const unionParent = (parent, a, b) => {
  const x = findParent(parent, a)
  const y = findParent(parent, b)
  if (x < y) {
    parent[y] = x
  } else {
    parent[x] = y
  }
}

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function (n, connections) {
  if (connections.length < n - 1) {
    return -1
  }

  const parent = Array.from({ length: n }, (v, i) => i)
  let edges = n - 1
  for (const [v, w] of connections) {
    if (edges === 0) {
      return 0
    }
    if (findParent(parent, v) !== findParent(parent, w)) {
      edges -= 1
      unionParent(parent, v, w)
    }
  }

  return edges
}
