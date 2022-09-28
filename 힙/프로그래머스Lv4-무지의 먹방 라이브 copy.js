// Queue 모듈로 풀기
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

function solution(food_times, k) {
  const total = food_times.reduce((a, b) => a + b)
  if (total <= k) {
    return -1
  }

  const temp = food_times.map((time, i) => [time, i + 1]).sort((a, b) => a[0] - b[0])

  const q = new Queue()
  temp.forEach((v) => q.enqueue(v))

  let prev = 0
  while (q.size > 0 && k >= 0) {
    const time = q.peek[0]
    const acc = (time - prev) * q.size
    if (k < acc) {
      break
    }
    q.dequeue()
    k -= acc
    prev = time
  }

  const items = []
  while (q.size) {
    items.push(q.dequeue())
  }

  const result = items.map((item) => item[1]).sort((a, b) => a - b)
  return result[k % result.length]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.31ms, 33.4MB)
// 테스트 2 〉	통과 (0.35ms, 33.5MB)
// 테스트 3 〉	통과 (0.47ms, 33.4MB)
// 테스트 4 〉	통과 (0.45ms, 33.4MB)
// 테스트 5 〉	통과 (0.32ms, 33.4MB)
// 테스트 6 〉	통과 (0.31ms, 33.5MB)
// 테스트 7 〉	통과 (0.32ms, 33.5MB)
// 테스트 8 〉	통과 (0.38ms, 33.5MB)
// 테스트 9 〉	통과 (0.31ms, 33.5MB)
// 테스트 10 〉	통과 (0.31ms, 33.4MB)
// 테스트 11 〉	통과 (0.31ms, 33.5MB)
// 테스트 12 〉	통과 (0.31ms, 33.4MB)
// 테스트 13 〉	통과 (0.33ms, 33.5MB)
// 테스트 14 〉	통과 (0.31ms, 33.5MB)
// 테스트 15 〉	통과 (0.42ms, 33.6MB)
// 테스트 16 〉	통과 (0.12ms, 33.4MB)
// 테스트 17 〉	통과 (0.48ms, 33.6MB)
// 테스트 18 〉	통과 (0.31ms, 33.6MB)
// 테스트 19 〉	통과 (0.10ms, 33.5MB)
// 테스트 20 〉	통과 (0.08ms, 33.5MB)
// 테스트 21 〉	통과 (0.46ms, 33.5MB)
// 테스트 22 〉	통과 (0.51ms, 33.5MB)
// 테스트 23 〉	통과 (0.08ms, 33.4MB)
// 테스트 24 〉	통과 (1.89ms, 33.6MB)
// 테스트 25 〉	통과 (3.83ms, 33.9MB)
// 테스트 26 〉	통과 (2.48ms, 33.8MB)
// 테스트 27 〉	통과 (2.68ms, 34MB)
// 테스트 28 〉	통과 (0.31ms, 33.4MB)
// 테스트 29 〉	통과 (0.31ms, 33.4MB)
// 테스트 30 〉	통과 (0.17ms, 33.4MB)
// 테스트 31 〉	통과 (0.20ms, 33.6MB)
// 테스트 32 〉	통과 (0.33ms, 33.4MB)
// 효율성  테스트
// 테스트 1 〉	통과 (278.38ms, 77.2MB)
// 테스트 2 〉	통과 (140.67ms, 78.6MB)
// 테스트 3 〉	통과 (275.16ms, 71.6MB)
// 테스트 4 〉	통과 (270.89ms, 76.2MB)
// 테스트 5 〉	통과 (310.79ms, 76.4MB)
// 테스트 6 〉	통과 (277.96ms, 79.3MB)
// 테스트 7 〉	통과 (299.88ms, 74.6MB)
// 테스트 8 〉	통과 (291.09ms, 79.4MB)

// stack으로 풀기
function solution(food_times, k) {
  const total = food_times.reduce((a, b) => a + b)
  if (total <= k) {
    return -1
  }

  const stack = food_times.map((time, i) => [time, i + 1]).sort((a, b) => b[0] - a[0])

  let prev = 0
  while (stack.length > 0 && k >= 0) {
    const time = stack[stack.length - 1][0]
    const acc = (time - prev) * stack.length
    if (k < acc) {
      break
    }
    stack.pop()
    k -= acc
    prev = time
  }

  const result = stack
    .reverse()
    .map((item) => item[1])
    .sort((a, b) => a - b)
  return result[k % result.length]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.27ms, 33.6MB)
// 테스트 2 〉	통과 (0.31ms, 33.5MB)
// 테스트 3 〉	통과 (0.21ms, 33.6MB)
// 테스트 4 〉	통과 (0.19ms, 33.5MB)
// 테스트 5 〉	통과 (0.27ms, 33.7MB)
// 테스트 6 〉	통과 (0.19ms, 33.7MB)
// 테스트 7 〉	통과 (0.31ms, 33.6MB)
// 테스트 8 〉	통과 (0.21ms, 33.6MB)
// 테스트 9 〉	통과 (0.19ms, 33.6MB)
// 테스트 10 〉	통과 (0.27ms, 33.6MB)
// 테스트 11 〉	통과 (0.19ms, 33.7MB)
// 테스트 12 〉	통과 (0.27ms, 33.5MB)
// 테스트 13 〉	통과 (0.27ms, 33.6MB)
// 테스트 14 〉	통과 (0.25ms, 33.5MB)
// 테스트 15 〉	통과 (0.25ms, 33.5MB)
// 테스트 16 〉	통과 (0.11ms, 33.5MB)
// 테스트 17 〉	통과 (0.19ms, 33.6MB)
// 테스트 18 〉	통과 (0.18ms, 33.6MB)
// 테스트 19 〉	통과 (0.07ms, 33.6MB)
// 테스트 20 〉	통과 (0.07ms, 33.6MB)
// 테스트 21 〉	통과 (0.26ms, 33.7MB)
// 테스트 22 〉	통과 (0.31ms, 33.7MB)
// 테스트 23 〉	통과 (0.07ms, 33.5MB)
// 테스트 24 〉	통과 (1.15ms, 33.8MB)
// 테스트 25 〉	통과 (3.07ms, 33.8MB)
// 테스트 26 〉	통과 (3.30ms, 33.8MB)
// 테스트 27 〉	통과 (2.01ms, 33.8MB)
// 테스트 28 〉	통과 (0.19ms, 33.5MB)
// 테스트 29 〉	통과 (0.19ms, 33.6MB)
// 테스트 30 〉	통과 (0.11ms, 33.6MB)
// 테스트 31 〉	통과 (0.10ms, 33.7MB)
// 테스트 32 〉	통과 (0.19ms, 33.6MB)
// 효율성  테스트
// 테스트 1 〉	통과 (234.53ms, 65.3MB)
// 테스트 2 〉	통과 (52.10ms, 65.7MB)
// 테스트 3 〉	통과 (188.46ms, 66.4MB)
// 테스트 4 〉	통과 (160.50ms, 66.3MB)
// 테스트 5 〉	통과 (186.17ms, 64.8MB)
// 테스트 6 〉	통과 (193.30ms, 68.4MB)
// 테스트 7 〉	통과 (187.76ms, 64.5MB)
// 테스트 8 〉	통과 (203.32ms, 69.1MB)

// 힙 모듈.. 아니 이거 왜 안되냐...
class Node {
  constructor(prior, value) {
    this.prior = prior
    this.value = value
  }

  get extract() {
    return [this.prior, this.value]
  }
}

class PriorityHeap {
  constructor() {
    this.items = [null]
  }

  get length() {
    return this.items.length - 1
  }

  get head() {
    if (this.items.length < 2) return
    return this.items[1]
  }

  // insert heapify
  _percolateUp() {
    let i = this.length
    let parent = Math.floor(i / 2)
    while (parent > 0) {
      if (this.items[i].prior < this.items[parent].prior) {
        let temp = this.items[parent]
        this.items[parent] = this.items[i]
        this.items[i] = temp
      }
      i = parent
      parent = Math.floor(i / 2)
    }
  }

  insert(prior, value) {
    const k = new Node(prior, value)
    this.items.push(k)
    this._percolateUp()
  }

  // pop heapify
  _percolateDown(idx) {
    let left = idx * 2
    let right = idx * 2 + 1
    let smallest = idx

    if (left <= this.length && this.items[left].prior < this.items[smallest].prior) {
      smallest = left
    }
    if (right < this.length && this.items[right].prior < this.items[smallest].prior) {
      smallest = right
    }
    if (smallest !== idx) {
      let temp = this.items[idx]
      this.items[idx] = this.items[smallest]
      this.items[smallest] = temp
      this._percolateDown(smallest)
    }
  }

  extract() {
    if (this.length === 0) return
    let extracted = this.items[1]
    this.items[1] = this.items[this.length]
    this.items.pop()
    this._percolateDown(1)
    return extracted.extract
  }
}

function solution(food_times, k) {
  const total = food_times.reduce((a, b) => a + b)
  if (total <= k) {
    return -1
  }

  const heap = new PriorityHeap()
  food_times.forEach((time, i) => heap.insert(time, i + 1))

  let prev = 0
  while (heap.head && k >= 0) {
    const time = heap.head.prior
    const acc = (time - prev) * heap.length
    if (k < acc) {
      break
    }
    heap.extract()
    k -= acc
    prev = time
  }

  const items = []
  while (heap.head) {
    items.push(heap.extract())
  }

  const result = items.map((item) => item[1]).sort((a, b) => a - b)
  return result[k % result.length]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.46ms, 33.7MB)
// 테스트 2 〉	통과 (0.58ms, 33.6MB)
// 테스트 3 〉	통과 (0.49ms, 33.5MB)
// 테스트 4 〉	통과 (0.63ms, 33.5MB)
// 테스트 5 〉	통과 (0.69ms, 33.4MB)
// 테스트 6 〉	통과 (0.47ms, 33.5MB)
// 테스트 7 〉	통과 (0.75ms, 33.7MB)
// 테스트 8 〉	통과 (0.46ms, 33.4MB)
// 테스트 9 〉	통과 (0.47ms, 33.6MB)
// 테스트 10 〉	통과 (0.46ms, 33.6MB)
// 테스트 11 〉	통과 (0.49ms, 33.4MB)
// 테스트 12 〉	통과 (0.71ms, 33.6MB)
// 테스트 13 〉	통과 (0.68ms, 33.6MB)
// 테스트 14 〉	통과 (0.56ms, 33.4MB)
// 테스트 15 〉	통과 (0.52ms, 33.5MB)
// 테스트 16 〉	통과 (0.13ms, 33.6MB)
// 테스트 17 〉	실패 (0.53ms, 33.5MB)
// 테스트 18 〉	실패 (0.75ms, 33.5MB)
// 테스트 19 〉	통과 (0.11ms, 33.5MB)
// 테스트 20 〉	통과 (0.09ms, 33.5MB)
// 테스트 21 〉	통과 (0.78ms, 33.7MB)
// 테스트 22 〉	통과 (1.01ms, 33.6MB)
// 테스트 23 〉	통과 (0.09ms, 33.5MB)
// 테스트 24 〉	통과 (5.03ms, 35.9MB)
// 테스트 25 〉	통과 (6.88ms, 36.1MB)
// 테스트 26 〉	통과 (7.34ms, 36.1MB)
// 테스트 27 〉	통과 (7.82ms, 36.2MB)
// 테스트 28 〉	통과 (0.67ms, 33.4MB)
// 테스트 29 〉	통과 (0.47ms, 33.5MB)
// 테스트 30 〉	통과 (0.31ms, 33.4MB)
// 테스트 31 〉	통과 (0.43ms, 33.5MB)
// 테스트 32 〉	통과 (0.52ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (321.92ms, 75.7MB)
// 테스트 2 〉	통과 (154.74ms, 77.6MB)
// 테스트 3 〉	통과 (243.19ms, 66.3MB)
// 테스트 4 〉	통과 (242.99ms, 68.1MB)
// 테스트 5 〉	통과 (272.49ms, 70.9MB)
// 테스트 6 〉	통과 (318.58ms, 76.2MB)
// 테스트 7 〉	통과 (275.00ms, 70.8MB)
// 테스트 8 〉	통과 (299.98ms, 79.2MB)
