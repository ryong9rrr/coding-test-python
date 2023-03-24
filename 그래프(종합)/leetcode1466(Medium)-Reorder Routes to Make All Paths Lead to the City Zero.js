// 접근 1 : DFS 1, visited 집합 자료형을 사용하는 방법
// - 시간복잡도 : O(N)
// - 공간복잡도 : O(N)
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function (n, connections) {
  const graph = Array.from({ length: n }, (v, i) => i).reduce((obj, node) => {
    if (!obj[node]) obj[node] = []
    return obj
  }, {})

  connections.forEach(([v, w]) => {
    graph[v].push([w, 1])
    graph[w].push([v, 0])
  })

  const visited = new Set([0])
  let count = 0
  const dfs = (node) => {
    graph[node].forEach(([child, sign]) => {
      if (!visited.has(child)) {
        visited.add(child)
        count += sign
        dfs(child)
      }
    })
  }

  dfs(0)

  return count
}

// 접근 2 : DFS 2, visited를 사용하지 않고 파라미터 하나(부모 노드)를 더 받는 방법
// - 시간복잡도 : O(N)
// - 공간복잡도 : O(N)
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function (n, connections) {
  const graph = Array.from({ length: n }, (v, i) => i).reduce((obj, node) => {
    if (!obj[node]) obj[node] = []
    return obj
  }, {})

  connections.forEach(([v, w]) => {
    graph[v].push([w, 1])
    graph[w].push([v, 0])
  })

  let count = 0
  const dfs = (parent, node) => {
    graph[node].forEach(([child, sign]) => {
      if (parent !== child) {
        count += sign
        dfs(node, child)
      }
    })
  }

  dfs(-1, 0)

  return count
}

// 접근 3 : BFS, 접근 1과 동일(visited 사용)한데 DFS가 아닌 BFS로 푼 것임
// - 시간복잡도 : O(N)
// - 공간복잡도 : O(N)
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function (n, connections) {
  const graph = Array.from({ length: n }, (v, i) => i).reduce((obj, node) => {
    if (!obj[node]) obj[node] = []
    return obj
  }, {})

  connections.forEach(([v, w]) => {
    graph[v].push([w, 1])
    graph[w].push([v, 0])
  })

  const q = [0] // 노드의 개수가 최대 50,000으로 작기 때문에 큐 자료구조가 아닌 그냥 배열을 사용했음.
  const visited = new Set([0])
  let count = 0
  while (q.length > 0) {
    const node = q.shift()
    graph[node].forEach(([child, sign]) => {
      if (!visited.has(child)) {
        visited.add(child)
        count += sign
        q.push(child)
      }
    })
  }

  return count
}
