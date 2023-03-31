// 매우 어려운 문제... ㅠㅠ

// 접근 1 (리트코드 솔루션 1) : DFS, 577ms(18.87%), 82.2MB(52.83%)
// - 시간복잡도, 공간복잡도 : O(N)
/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function (edges) {
  const n = edges.length
  const visited = new Set()
  let ans = -1

  const dfs = (node, dist) => {
    const neighbor = edges[node]
    if (neighbor === -1) {
      return
    }

    if (!visited.has(neighbor)) {
      dist[neighbor] = dist[node] + 1
      visited.add(neighbor)
      dfs(neighbor, dist)
      return
    }

    if (dist[neighbor]) {
      ans = Math.max(ans, dist[node] - dist[neighbor] + 1)
    }
  }

  for (let node = 0; node < n; node += 1) {
    if (!visited.has(node)) {
      const dist = {}
      dist[node] = 1
      visited.add(node)
      dfs(node, dist)
    }
  }

  return ans
}

// 접근 2 (리트코드 솔루션 2) : Kahn's Alogirhtm(위상정렬), 218ms(92.45%), 78.8MB(79.25%)
// - 시간복잡도, 공간복잡도 : O(N)
class MyNode {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class MyQueue {
  constructor(array = []) {
    this.front = this.tail = null
    this.size = 0

    for (const el of array) {
      this.enqueue(el)
    }
  }

  get peek() {
    return !this.front || !this.tail ? undefined : this.front.value
  }

  enqueue(value) {
    const node = new MyNode(value)
    if (!this.front) {
      this.front = this.tail = node
    } else {
      this.tail = this.tail.next = node
    }
    this.size += 1
  }

  dequeue() {
    if (!this.front) {
      return undefined
    }
    const result = this.front.value
    this.front = this.front.next
    this.size -= 1
    return result
  }
}

/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function (edges) {
  const n = edges.length
  const visited = new Set()
  const indegree = new Array(n).fill(0)
  edges.forEach((w) => {
    if (w !== -1) {
      indegree[w] += 1
    }
  })

  const q = new MyQueue()
  for (let v = 0; v < n; v += 1) {
    if (indegree[v] === 0) {
      q.enqueue(v)
    }
  }

  while (q.size > 0) {
    const v = q.dequeue()
    visited.add(v)
    const w = edges[v]
    if (w !== -1) {
      indegree[w] -= 1
      if (indegree[w] === 0) {
        q.enqueue(w)
      }
    }
  }

  let ans = -1
  for (let v = 0; v < n; v += 1) {
    if (!visited.has(v)) {
      visited.add(v)
      let w = edges[v]
      let count = 1
      while (v !== w) {
        visited.add(w)
        count += 1
        w = edges[w]
      }
      ans = Math.max(ans, count)
    }
  }

  return ans
}
