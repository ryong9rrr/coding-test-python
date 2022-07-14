// 그냥 shift로
function solution(tickets) {
  tickets.sort()
  const graph = {}
  for (const [v, w] of tickets) {
    if (!graph[v]) graph[v] = []
    graph[v].push(w)
  }

  const routes = []

  function dfs(v) {
    while (graph[v] && graph[v].length > 0) {
      dfs(graph[v].shift())
    }
    routes.push(v)
  }

  dfs('ICN')
  return routes.reverse()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.18ms, 30.3MB)
// 테스트 2 〉	통과 (0.27ms, 29.8MB)
// 테스트 3 〉	통과 (0.37ms, 29.9MB)
// 테스트 4 〉	통과 (0.31ms, 30.1MB)

// 큐를 구현해서 풀기
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

function solution(tickets) {
  tickets.sort()
  const graph = {}
  for (const [v, w] of tickets) {
    if (!graph[v]) graph[v] = new Queue()
    graph[v].enqueue(w)
  }

  const routes = []

  function dfs(v) {
    while (graph[v] && graph[v].size > 0) {
      dfs(graph[v].dequeue())
    }
    routes.push(v)
  }

  dfs('ICN')
  return routes.reverse()
}

//   정확성  테스트
//   테스트 1 〉	통과 (0.42ms, 29.9MB)
//   테스트 2 〉	통과 (0.32ms, 29.8MB)
//   테스트 3 〉	통과 (0.34ms, 29.9MB)
//   테스트 4 〉	통과 (0.21ms, 29.9MB)
