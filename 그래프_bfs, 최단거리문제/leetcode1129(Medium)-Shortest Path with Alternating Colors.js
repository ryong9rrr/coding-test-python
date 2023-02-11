// 119ms(33.33%), 50.8MB(11.49%)
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

const initiailizeGraph = (n) => {
  const graph = {}
  for (let i = 0; i < n; i += 1) {
    graph[i] = []
  }
  return graph
}

/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */
var shortestAlternatingPaths = function (n, redEdges, blueEdges) {
  const RED = 0
  const BLUE = 1
  const graph = initiailizeGraph(n)
  for (const [v, w] of redEdges) {
    graph[v].push([w, RED])
  }
  for (const [v, w] of blueEdges) {
    graph[v].push([w, BLUE])
  }

  const visited = Array.from({ length: n }, () => new Array(2).fill(false))
  const answer = new Array(n).fill(Infinity)
  answer[0] = 0
  const q = new MyQueue()
  for (const [_, color] of graph[0]) {
    visited[0][color] = true
    q.enqueue([0, null, 0]) // node, unknown-color, dist
  }

  while (q.size > 0) {
    const [v, prevColor, dist] = q.dequeue()
    for (const [w, color] of graph[v]) {
      if (color !== prevColor && !visited[w][color]) {
        visited[w][color] = true
        q.enqueue([w, color, dist + 1])
        answer[w] = Math.min(answer[w], dist + 1)
      }
    }
  }

  return answer.map((x) => (x === Infinity ? -1 : x))
}
