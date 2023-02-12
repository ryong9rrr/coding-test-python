// 접근 1 - dfs + 백트래킹 : O(N), 534ms(75%) 98.6MB(82.14%)
/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function (roads, seats) {
  const adj = roads.reduce((obj, [v, w]) => {
    if (!obj[v]) obj[v] = []
    if (!obj[w]) obj[w] = []
    obj[v].push(w)
    obj[w].push(v)
    return obj
  }, {})

  let fuel = 0

  const dfs = (node, parent) => {
    representatives = 1
    if (!(node in adj)) {
      return representatives
    }

    for (const child of adj[node]) {
      if (child !== parent) {
        representatives += dfs(child, node)
      }
    }

    if (node !== 0) {
      fuel += Math.ceil(representatives / seats)
    }

    return representatives
  }

  dfs(0, null)

  return fuel
}

// 접근 2 - 위상정렬(BFS) : 484ms(96.43%), 109.7MB(50%)
class MyNode {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class MyQueue {
  constructor() {
    this.front = this.tail = null
    this.size = 0
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

const intializeAdj = (n) => {
  const result = {}
  for (let i = 0; i < n; i += 1) {
    result[i] = []
  }
  return result
}

/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function (roads, seats) {
  const n = roads.length + 1
  const degrees = new Array(n).fill(0)
  const adj = intializeAdj(n)
  // 그래프(adj), 간선정보(degrees) 초기화
  roads.forEach(([v, w]) => {
    degrees[v] += 1
    degrees[w] += 1
    adj[v].push(w)
    adj[w].push(v)
  })

  // 위상정렬(BFS)
  const representatives = new Array(n).fill(1)
  const q = new MyQueue()
  for (let v = 1; v < n; v += 1) {
    if (degrees[v] === 1) {
      q.enqueue(v)
    }
  }

  let fuel = 0
  while (q.size > 0) {
    const v = q.dequeue()
    fuel += Math.ceil(representatives[v] / seats)

    for (const w of adj[v]) {
      degrees[w] -= 1
      representatives[w] += representatives[v]
      if (w !== 0 && degrees[w] === 1) {
        q.enqueue(w)
      }
    }
  }

  return fuel
}
