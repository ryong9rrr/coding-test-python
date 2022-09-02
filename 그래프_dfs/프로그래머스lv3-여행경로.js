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
  const graph = [...tickets].sort().reduce((acc, [v, w]) => {
    if (!acc[v]) acc[v] = new Queue()
    acc[v].enqueue(w)
    return acc
  }, {})

  const result = []

  const dfs = (v) => {
    while (graph[v] instanceof Queue && graph[v].size > 0) {
      dfs(graph[v].dequeue())
    }
    result.push(v)
  }

  dfs('ICN')

  return result.reverse()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.36ms, 33.2MB)
// 테스트 2 〉	통과 (0.20ms, 33.5MB)
// 테스트 3 〉	통과 (0.27ms, 33.4MB)
// 테스트 4 〉	통과 (0.18ms, 33.4MB)

// 반복문 + stack
function solution(tickets) {
  const graph = tickets.reduce((acc, [v, w]) => {
    if (!acc[v]) acc[v] = []
    acc[v].push(w)
    return acc
  }, {})

  for (const v in graph) {
    // 스택으로 사용하기 위해 역순으로 정렬
    graph[v].sort((a, b) => (a < b ? 1 : -1))
  }

  const stack = ['ICN']
  const result = []

  while (stack.length > 0) {
    const v = stack[stack.length - 1]
    if (graph[v] && graph[v].length > 0) {
      stack.push(graph[v].pop())
    } else {
      result.push(stack.pop())
    }
  }

  return result.reverse()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.35ms, 33.6MB)
// 테스트 2 〉	통과 (0.11ms, 33.5MB)
// 테스트 3 〉	통과 (0.15ms, 33.5MB)
// 테스트 4 〉	통과 (0.10ms, 33.6MB)
