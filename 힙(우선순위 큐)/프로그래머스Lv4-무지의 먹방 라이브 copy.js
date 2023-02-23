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
