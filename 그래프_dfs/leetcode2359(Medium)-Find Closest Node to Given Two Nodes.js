// 177ms(85.71%), 81.2MB(42.86%)
/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function (edges, node1, node2) {
  const N = edges.length
  const graph = edges.reduce((obj, w, v) => {
    obj[v] = w
    return obj
  }, {})

  const dfs = (v, visited, dist, depth) => {
    visited[v] = true
    dist[v] = depth
    const w = graph[v]
    if (!visited[w] && w !== -1) {
      dfs(w, visited, dist, depth + 1)
    }
  }

  const visited1 = new Array(N).fill(false)
  const dist1 = new Array(N).fill(0)

  const visited2 = new Array(N).fill(false)
  const dist2 = new Array(N).fill(0)

  dfs(node1, visited1, dist1, 0)
  dfs(node2, visited2, dist2, 0)

  let minDist = Infinity
  let result = -1
  for (let v = 0; v < N; v++) {
    const currentMax = Math.max(dist1[v], dist2[v])
    if (visited1[v] && visited2[v] && minDist > currentMax) {
      minDist = currentMax
      result = v
    }
  }

  return result
}
