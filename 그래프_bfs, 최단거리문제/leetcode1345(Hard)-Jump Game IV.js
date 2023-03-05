// 301ms(81.25%), 77.3MB(56.25%)
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

  get desc() {
    const result = []
    let node = this.front
    while (node) {
      result.push(node.value)
      node = node.next
    }
    return result.join(" ")
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

const initializeGraph = (arr) => {
  const graph = {}
  for (let i = 0; i < arr.length; i += 1) {
    const num = arr[i]
    if (!graph[num]) graph[num] = []
    graph[num].push(i)
  }
  return graph
}

/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function (arr) {
  const n = arr.length
  if (n <= 1) {
    return 0
  }

  const graph = initializeGraph(arr)
  const q = new MyQueue()
  const dist = new Array(n).fill(-1)

  q.enqueue(n - 1)
  dist[n - 1] = 0

  while (q.size > 0) {
    const index = q.dequeue()
    const num = arr[index]

    graph[num].forEach((i) => {
      if (dist[i] === -1) {
        dist[i] = dist[index] + 1
        q.enqueue(i)
      }
    })

    graph[num] = []

    const neighbors = [index - 1, index + 1]
    neighbors.forEach((i) => {
      if (i >= 0 && i < n && dist[i] === -1) {
        dist[i] = dist[index] + 1
        q.enqueue(i)
      }
    })

    if (dist[0] !== -1) {
      break
    }
  }

  return dist[0]
}
