// (1) 큐를 사용한 풀이
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

function solution(food_times, k) {
  const total = food_times.reduce((a, b) => a + b)

  if (total <= k) {
    return -1
  }

  const foods = food_times
    .map((time, i) => [time, i + 1])
    .sort((a, b) => a[0] - b[0])

  const q = new MyQueue(foods)

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
  while (q.size > 0) {
    items.push(q.dequeue())
  }

  const result = items.map((item) => item[1]).sort((a, b) => a - b)
  return result[k % result.length]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.32ms, 33.4MB)
// 테스트 2 〉	통과 (0.47ms, 32.9MB)
// 테스트 3 〉	통과 (0.52ms, 33.4MB)
// 테스트 4 〉	통과 (0.46ms, 33.4MB)
// 테스트 5 〉	통과 (0.33ms, 33.4MB)
// 테스트 6 〉	통과 (0.32ms, 33.5MB)
// 테스트 7 〉	통과 (0.33ms, 33.4MB)
// 테스트 8 〉	통과 (0.35ms, 33.5MB)
// 테스트 9 〉	통과 (0.32ms, 33.4MB)
// 테스트 10 〉	통과 (0.32ms, 33.4MB)
// 테스트 11 〉	통과 (0.32ms, 33.4MB)
// 테스트 12 〉	통과 (0.31ms, 33.3MB)
// 테스트 13 〉	통과 (0.32ms, 33.4MB)
// 테스트 14 〉	통과 (0.32ms, 33.5MB)
// 테스트 15 〉	통과 (0.31ms, 33.4MB)
// 테스트 16 〉	통과 (0.07ms, 33.3MB)
// 테스트 17 〉	통과 (0.34ms, 33.5MB)
// 테스트 18 〉	통과 (0.32ms, 33.4MB)
// 테스트 19 〉	통과 (0.07ms, 33.5MB)
// 테스트 20 〉	통과 (0.12ms, 33.4MB)
// 테스트 21 〉	통과 (0.49ms, 33.5MB)
// 테스트 22 〉	통과 (0.58ms, 33.4MB)
// 테스트 23 〉	통과 (0.09ms, 33.4MB)
// 테스트 24 〉	통과 (1.83ms, 33.7MB)
// 테스트 25 〉	통과 (2.57ms, 33.9MB)
// 테스트 26 〉	통과 (2.66ms, 33.8MB)
// 테스트 27 〉	통과 (4.16ms, 33.9MB)
// 테스트 28 〉	통과 (0.33ms, 33.4MB)
// 테스트 29 〉	통과 (0.43ms, 33.4MB)
// 테스트 30 〉	통과 (0.19ms, 33.3MB)
// 테스트 31 〉	통과 (0.21ms, 33.4MB)
// 테스트 32 〉	통과 (0.38ms, 33.4MB)
// 효율성  테스트
// 테스트 1 〉	통과 (325.41ms, 81.4MB)
// 테스트 2 〉	통과 (151.03ms, 82.8MB)
// 테스트 3 〉	통과 (235.09ms, 79.9MB)
// 테스트 4 〉	통과 (256.60ms, 79.6MB)
// 테스트 5 〉	통과 (308.99ms, 83.8MB)
// 테스트 6 〉	통과 (325.24ms, 82.2MB)
// 테스트 7 〉	통과 (305.31ms, 82.1MB)
// 테스트 8 〉	통과 (359.42ms, 83.5MB)

// (2) stack을 사용한 풀기
function solution(food_times, k) {
  const total = food_times.reduce((a, b) => a + b)

  if (total <= k) {
    return -1
  }

  const stack = food_times
    .map((time, i) => [time, i + 1])
    .sort((a, b) => b[0] - a[0])

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

  return stack
    .reverse()
    .map((item) => item[1])
    .sort((a, b) => a - b)[k % stack.length]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.19ms, 33.5MB)
// 테스트 2 〉	통과 (0.19ms, 33.5MB)
// 테스트 3 〉	통과 (0.19ms, 33.5MB)
// 테스트 4 〉	통과 (0.19ms, 33.4MB)
// 테스트 5 〉	통과 (0.19ms, 33.4MB)
// 테스트 6 〉	통과 (0.18ms, 33.5MB)
// 테스트 7 〉	통과 (0.19ms, 33.4MB)
// 테스트 8 〉	통과 (0.25ms, 33.5MB)
// 테스트 9 〉	통과 (0.18ms, 33.6MB)
// 테스트 10 〉	통과 (0.19ms, 33.3MB)
// 테스트 11 〉	통과 (0.30ms, 33.5MB)
// 테스트 12 〉	통과 (0.21ms, 33.4MB)
// 테스트 13 〉	통과 (0.18ms, 33.5MB)
// 테스트 14 〉	통과 (0.18ms, 33.6MB)
// 테스트 15 〉	통과 (0.18ms, 33.3MB)
// 테스트 16 〉	통과 (0.07ms, 33.6MB)
// 테스트 17 〉	통과 (0.18ms, 33.5MB)
// 테스트 18 〉	통과 (0.19ms, 33.4MB)
// 테스트 19 〉	통과 (0.07ms, 33.6MB)
// 테스트 20 〉	통과 (0.11ms, 33.5MB)
// 테스트 21 〉	통과 (0.26ms, 33.4MB)
// 테스트 22 〉	통과 (0.40ms, 33.4MB)
// 테스트 23 〉	통과 (0.07ms, 33.4MB)
// 테스트 24 〉	통과 (1.13ms, 33.6MB)
// 테스트 25 〉	통과 (3.05ms, 33.7MB)
// 테스트 26 〉	통과 (3.37ms, 33.6MB)
// 테스트 27 〉	통과 (1.95ms, 33.8MB)
// 테스트 28 〉	통과 (0.18ms, 33.4MB)
// 테스트 29 〉	통과 (0.19ms, 33.5MB)
// 테스트 30 〉	통과 (0.08ms, 33.5MB)
// 테스트 31 〉	통과 (0.16ms, 33.5MB)
// 테스트 32 〉	통과 (0.30ms, 33.4MB)
// 효율성  테스트
// 테스트 1 〉	통과 (196.32ms, 65.6MB)
// 테스트 2 〉	통과 (46.54ms, 65MB)
// 테스트 3 〉	통과 (176.01ms, 65.9MB)
// 테스트 4 〉	통과 (196.79ms, 68.4MB)
// 테스트 5 〉	통과 (185.72ms, 63.9MB)
// 테스트 6 〉	통과 (264.62ms, 66.1MB)
// 테스트 7 〉	통과 (201.33ms, 64.1MB)
// 테스트 8 〉	통과 (197.63ms, 70.2MB)

// Heap 모듈 구현
class Heap {
  constructor(compareFn) {
    this.values = []

    this.compareFn = compareFn
  }

  compare(a, b) {
    if (a === undefined || b === undefined) {
      return false
    }

    const result = this.compareFn(a, b)
    if (typeof result === "boolean") {
      return result
    }
    return result < 0 ? true : false
  }

  get top() {
    return this.values.length > 0 ? this.values[0] : undefined
  }

  get size() {
    return this.values.length
  }

  add(element) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  extract() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    const top = this.values[0]
    const end = this.values.pop()

    if (this.values.length > 0) {
      this.values[0] = end
      this.percolateDown(0)
    }

    // return the top
    return top
  }

  swap(aIndex, bIndex) {
    ;[this.values[aIndex], this.values[bIndex]] = [
      this.values[bIndex],
      this.values[aIndex],
    ]
  }

  parent(index) {
    return Math.floor(Math.floor((index - 1) / 2))
  }

  leftChild(index) {
    return index * 2 + 1
  }

  rightChild(index) {
    return index * 2 + 2
  }

  isLeaf(index) {
    return (
      index >= Math.floor(this.values.length / 2) &&
      index <= this.values.length - 1
    )
  }

  percolateUp(index) {
    let currentIndex = index
    let parentIndex = this.parent(currentIndex)

    while (
      currentIndex > 0 &&
      this.compare(this.values[currentIndex], this.values[parentIndex])
    ) {
      this.swap(currentIndex, parentIndex)
      currentIndex = parentIndex
      parentIndex = this.parent(parentIndex)
    }
  }

  percolateDown(index) {
    if (!this.isLeaf(index)) {
      let leftChildIndex = this.leftChild(index)
      let rightChildIndex = this.rightChild(index)
      let largestIndex = index

      if (
        this.compare(this.values[leftChildIndex], this.values[largestIndex])
      ) {
        largestIndex = leftChildIndex
      }

      if (
        this.compare(this.values[rightChildIndex], this.values[largestIndex])
      ) {
        largestIndex = rightChildIndex
      }

      if (largestIndex !== index) {
        this.swap(index, largestIndex)
        this.percolateDown(largestIndex)
      }
    }
  }
}

const sum = (array) => {
  return array.reduce((a, b) => a + b, 0)
}

function solution(food_times, k) {
  if (sum(food_times) <= k) {
    return -1
  }

  const heap = new Heap((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]))
  food_times.forEach((time, i) => {
    heap.add([time, i + 1])
  })

  let prev = 0
  while (heap.size > 0 && k >= 0) {
    const [time] = heap.top
    const acc = (time - prev) * heap.size
    if (k < acc) {
      break
    }

    heap.extract()
    k -= acc
    prev = time
  }

  const result = [...heap.values].map(([time, i]) => i).sort((a, b) => a - b)

  return result[k % result.length]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.58ms, 33.4MB)
// 테스트 2 〉	통과 (0.54ms, 33.6MB)
// 테스트 3 〉	통과 (0.58ms, 33MB)
// 테스트 4 〉	통과 (0.60ms, 33.1MB)
// 테스트 5 〉	통과 (0.56ms, 33.5MB)
// 테스트 6 〉	통과 (0.87ms, 33.5MB)
// 테스트 7 〉	통과 (0.58ms, 33.6MB)
// 테스트 8 〉	통과 (0.56ms, 33.5MB)
// 테스트 9 〉	통과 (0.59ms, 33.5MB)
// 테스트 10 〉	통과 (0.65ms, 33.5MB)
// 테스트 11 〉	통과 (0.88ms, 33.5MB)
// 테스트 12 〉	통과 (0.64ms, 33.6MB)
// 테스트 13 〉	통과 (0.62ms, 33.5MB)
// 테스트 14 〉	통과 (1.00ms, 33.5MB)
// 테스트 15 〉	통과 (0.69ms, 33.5MB)
// 테스트 16 〉	통과 (0.15ms, 33.4MB)
// 테스트 17 〉	통과 (0.70ms, 33.5MB)
// 테스트 18 〉	통과 (0.63ms, 33.5MB)
// 테스트 19 〉	통과 (0.10ms, 33.5MB)
// 테스트 20 〉	통과 (0.13ms, 33.5MB)
// 테스트 21 〉	통과 (1.21ms, 33.6MB)
// 테스트 22 〉	통과 (1.34ms, 33.8MB)
// 테스트 23 〉	통과 (0.09ms, 33.5MB)
// 테스트 24 〉	통과 (6.55ms, 37MB)
// 테스트 25 〉	통과 (6.61ms, 36.6MB)
// 테스트 26 〉	통과 (8.01ms, 36.8MB)
// 테스트 27 〉	통과 (6.32ms, 36.5MB)
// 테스트 28 〉	통과 (0.68ms, 33.5MB)
// 테스트 29 〉	통과 (0.86ms, 33.4MB)
// 테스트 30 〉	통과 (0.21ms, 33.5MB)
// 테스트 31 〉	통과 (0.28ms, 33.4MB)
// 테스트 32 〉	통과 (0.85ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (221.25ms, 76.9MB)
// 테스트 2 〉	통과 (88.61ms, 71.1MB)
// 테스트 3 〉	통과 (274.93ms, 74.1MB)
// 테스트 4 〉	통과 (270.34ms, 75.3MB)
// 테스트 5 〉	통과 (236.49ms, 77.2MB)
// 테스트 6 〉	통과 (230.20ms, 77.2MB)
// 테스트 7 〉	통과 (248.94ms, 73.9MB)
// 테스트 8 〉	통과 (196.62ms, 78.4MB)
