// 파이썬과 동일한 풀이, 시간이 엄청 오래걸리는데, shift 사용때문으로 보임
function makeGraph(vertexArray) {
  const graph = {}
  for (const [v, w] of vertexArray) {
    if (!graph[v]) graph[v] = []
    if (!graph[w]) graph[w] = []
    graph[v].push(w)
    graph[w].push(v)
  }
  return graph
}

function solution(n, edge) {
  const graph = makeGraph(edge)
  // const visited = Array(n + 1).fill(0) 와 같다.
  const visited = Array.from({ length: n + 1 }, (v, i) => 0)
  const q = []

  q.push([1, 1])
  while (q.length > 0) {
    const [v, distance] = q.shift()
    if (visited[v]) continue
    visited[v] += distance
    for (const w of graph[v]) {
      if (visited[w]) continue
      q.push([w, distance + 1])
    }
  }

  const maxDistance = Math.max(...visited)
  return visited.filter((v) => v === maxDistance).length
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.33ms, 29.9MB)
// 테스트 2 〉	통과 (0.40ms, 30MB)
// 테스트 3 〉	통과 (0.42ms, 30MB)
// 테스트 4 〉	통과 (0.75ms, 30.1MB)
// 테스트 5 〉	통과 (2.02ms, 30.4MB)
// 테스트 6 〉	통과 (17.07ms, 35.1MB)
// 테스트 7 〉	통과 (84.55ms, 48.1MB)
// 테스트 8 〉	통과 (42.92ms, 55.5MB)
// 테스트 9 〉	통과 (7621.53ms, 57.5MB)

// 직접 구현한 큐, 효과는 굉장했다.
class Node {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class Queue {
  constructor() {
    this.front = this.tail = null
    this.size = 0
  }

  get peek() {
    return (this.front && this.front.value) || null
  }

  enqueue(newValue) {
    const newNode = new Node(newValue)
    if (!this.front) {
      this.front = this.tail = newNode
    } else {
      this.tail = this.tail.next = newNode
    }
    this.size++
  }

  dequeue() {
    if (!this.front) return null
    const extracted = this.front.value
    this.front = this.front.next
    this.size--
    return extracted
  }
}

function solution(n, edge) {
  const graph = {}
  edge.forEach(([v, w]) => {
    if (!graph[v]) graph[v] = []
    if (!graph[w]) graph[w] = []
    graph[v].push(w)
    graph[w].push(v)
  })

  // const visited = Array(n + 1).fill(0) 와 같다.
  const visited = Array.from({ length: n + 1 }, (v, i) => 0)
  const q = new Queue()
  q.enqueue([1, 1])

  while (q.size > 0) {
    const [v, distance] = q.dequeue()
    if (visited[v] !== 0) {
      continue
    }
    visited[v] += distance
    for (const w of graph[v]) {
      q.enqueue([w, distance + 1])
    }
  }

  const max = Math.max(...visited)
  return visited.filter((v) => v === max).length
}

/*
정확성  테스트
테스트 1 〉	통과 (0.43ms, 30.4MB)
테스트 2 〉	통과 (0.46ms, 30.2MB)
테스트 3 〉	통과 (0.48ms, 30.2MB)
테스트 4 〉	통과 (1.07ms, 30.3MB)
테스트 5 〉	통과 (4.45ms, 32.9MB)
테스트 6 〉	통과 (15.17ms, 36MB)
테스트 7 〉	통과 (26.67ms, 51.6MB)
테스트 8 〉	통과 (31.81ms, 58MB)
테스트 9 〉	통과 (46.80ms, 63.9MB)
*/

// 22년 9월 풀이
class Node {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class Queue {
  constructor() {
    this.front = this.tail = null
    this.size = 0
  }

  get peek() {
    return (this.front && this.front.value) || null
  }

  enqueue(newValue) {
    const newNode = new Node(newValue)
    if (!this.front) {
      this.front = this.tail = newNode
    } else {
      this.tail = this.tail.next = newNode
    }
    this.size++
  }

  dequeue() {
    if (!this.front) return null
    const extracted = this.front.value
    this.front = this.front.next
    this.size--
    return extracted
  }
}

function solution(n, edge) {
  const graph = {}
  for (const [v, w] of edge) {
    if (!graph[v]) graph[v] = []
    if (!graph[w]) graph[w] = []
    graph[v].push(w)
    graph[w].push(v)
  }

  const distance = Array.from({ length: n + 1 }, () => -1)

  const q = new Queue()
  q.enqueue(1)
  distance[1] = 0

  while (q.size > 0) {
    const v = q.dequeue()
    for (const w of graph[v]) {
      if (distance[w] !== -1) continue
      distance[w] = distance[v] + 1
      q.enqueue(w)
    }
  }

  const maxValue = Math.max(...distance)
  return distance.filter((x) => x === maxValue).length
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.26ms, 33.5MB)
// 테스트 2 〉	통과 (0.39ms, 33.6MB)
// 테스트 3 〉	통과 (0.39ms, 33.6MB)
// 테스트 4 〉	통과 (0.63ms, 33.8MB)
// 테스트 5 〉	통과 (2.70ms, 34.4MB)
// 테스트 6 〉	통과 (3.32ms, 35.5MB)
// 테스트 7 〉	통과 (36.25ms, 48.6MB)
// 테스트 8 〉	통과 (35.87ms, 56.4MB)
// 테스트 9 〉	통과 (37.98ms, 56MB)
