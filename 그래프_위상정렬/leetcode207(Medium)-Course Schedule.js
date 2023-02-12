// 위상정렬 : 90ms, 46.3MB
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const indegree = new Array(numCourses).fill(0)
  const graph = prerequisites.reduce((obj, [v, w]) => {
    if (!obj[v]) obj[v] = []
    obj[v].push(w)
    indegree[w] += 1
    return obj
  }, {})

  const q = []
  for (let node = 0; node < numCourses; node += 1) {
    if (indegree[node] === 0) {
      q.push(node)
    }
  }

  let count = 0
  while (q.length > 0) {
    count += 1
    v = q.shift()
    if (!graph[v]) {
      continue
    }
    for (const w of graph[v]) {
      indegree[w] -= 1
      if (indegree[w] === 0) {
        q.push(w)
      }
    }
  }

  return count === numCourses
}

// dfs : 75ms, 46.6MB
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const graph = prerequisites.reduce((obj, [v, w]) => {
    if (!obj[v]) obj[v] = []
    obj[v].push(w)
    return obj
  }, {})

  const traced = new Set()
  const visited = new Set()

  const dfs = (v) => {
    if (traced.has(v)) {
      return false
    }
    if (visited.has(v)) {
      return true
    }
    traced.add(v)
    if (graph[v]) {
      for (const w of graph[v]) {
        if (!dfs(w)) {
          return false
        }
      }
    }
    traced.delete(v)
    visited.add(v)
    return true
  }

  for (const v of Object.keys(graph)) {
    if (!dfs(v)) {
      return false
    }
  }
  return true
}
