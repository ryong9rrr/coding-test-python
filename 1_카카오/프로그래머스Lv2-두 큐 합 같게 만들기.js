// Queue 풀이
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

function sum(array) {
  return array.reduce((a, b) => a + b, 0)
}

function solution(queue1, queue2) {
  const LIMIT = queue1.length * 4

  let aSum = sum(queue1)
  let bSum = sum(queue2)
  const aQueue = new MyQueue(queue1)
  const bQueue = new MyQueue(queue2)

  let answer = 0
  while (aQueue.size > 0 && bQueue.size > 0 && answer < LIMIT) {
    if (aSum < bSum) {
      const x = bQueue.dequeue()
      bSum -= x
      aQueue.enqueue(x)
      aSum += x
      answer += 1
    } else if (aSum > bSum) {
      const x = aQueue.dequeue()
      aSum -= x
      bQueue.enqueue(x)
      bSum += x
      answer += 1
    } else {
      return answer
    }
  }

  return -1
}
//   정확성  테스트
//   테스트 1 〉	통과 (0.26ms, 33.4MB)
//   테스트 2 〉	통과 (0.15ms, 33.4MB)
//   테스트 3 〉	통과 (0.25ms, 33.4MB)
//   테스트 4 〉	통과 (0.27ms, 33.4MB)
//   테스트 5 〉	통과 (0.34ms, 33.5MB)
//   테스트 6 〉	통과 (0.36ms, 33.5MB)
//   테스트 7 〉	통과 (0.36ms, 33.6MB)
//   테스트 8 〉	통과 (0.46ms, 33.5MB)
//   테스트 9 〉	통과 (0.68ms, 33.6MB)
//   테스트 10 〉	통과 (1.16ms, 33.8MB)
//   테스트 11 〉	통과 (35.44ms, 56.7MB)
//   테스트 12 〉	통과 (23.45ms, 46.3MB)
//   테스트 13 〉	통과 (56.57ms, 50.9MB)
//   테스트 14 〉	통과 (35.96ms, 50.5MB)
//   테스트 15 〉	통과 (70.42ms, 53.4MB)
//   테스트 16 〉	통과 (28.48ms, 52.9MB)
//   테스트 17 〉	통과 (32.99ms, 50.3MB)
//   테스트 18 〉	통과 (96.97ms, 80.6MB)
//   테스트 19 〉	통과 (131.40ms, 81.4MB)
//   테스트 20 〉	통과 (109.43ms, 80.6MB)
//   테스트 21 〉	통과 (114.83ms, 83.3MB)
//   테스트 22 〉	통과 (134.25ms, 89.6MB)
//   테스트 23 〉	통과 (121.18ms, 83.2MB)
//   테스트 24 〉	통과 (131.17ms, 89.1MB)
//   테스트 25 〉	통과 (0.56ms, 33.4MB)
//   테스트 26 〉	통과 (0.35ms, 33.5MB)
//   테스트 27 〉	통과 (0.38ms, 33.4MB)
//   테스트 28 〉	통과 (101.96ms, 70.7MB)
//   테스트 29 〉	통과 (7.55ms, 37.7MB)
//   테스트 30 〉	통과 (66.43ms, 64.9MB)

// 포인터
function sum(array) {
  return array.reduce((a, b) => a + b, 0)
}

function solution(queue1, queue2) {
  const LIMIT = queue1.length * 4

  let aIndex = 0
  let bIndex = 0
  let aSum = sum(queue1)
  let bSum = sum(queue2)

  let answer = 0
  while (aIndex < queue1.length && bIndex < queue2.length && answer < LIMIT) {
    if (aSum < bSum) {
      const x = queue2[bIndex]
      bIndex += 1
      bSum -= x
      queue1.push(x)
      aSum += x
      answer += 1
    } else if (aSum > bSum) {
      const x = queue1[aIndex]
      aIndex += 1
      aSum -= x
      queue2.push(x)
      bSum += x
      answer += 1
    } else {
      return answer
    }
  }

  return -1
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 33.4MB)
// 테스트 2 〉	통과 (0.07ms, 33.4MB)
// 테스트 3 〉	통과 (0.11ms, 33.4MB)
// 테스트 4 〉	통과 (0.11ms, 33.4MB)
// 테스트 5 〉	통과 (0.17ms, 33.4MB)
// 테스트 6 〉	통과 (0.24ms, 33.5MB)
// 테스트 7 〉	통과 (0.20ms, 33.5MB)
// 테스트 8 〉	통과 (0.25ms, 33.6MB)
// 테스트 9 〉	통과 (0.34ms, 33.4MB)
// 테스트 10 〉	통과 (0.38ms, 33.5MB)
// 테스트 11 〉	통과 (16.12ms, 42.5MB)
// 테스트 12 〉	통과 (8.72ms, 38MB)
// 테스트 13 〉	통과 (6.83ms, 39.9MB)
// 테스트 14 〉	통과 (8.25ms, 40.8MB)
// 테스트 15 〉	통과 (11.57ms, 42MB)
// 테스트 16 〉	통과 (7.28ms, 42MB)
// 테스트 17 〉	통과 (7.32ms, 39.7MB)
// 테스트 18 〉	통과 (20.94ms, 54.1MB)
// 테스트 19 〉	통과 (24.50ms, 55.2MB)
// 테스트 20 〉	통과 (25.82ms, 56.2MB)
// 테스트 21 〉	통과 (21.21ms, 56.4MB)
// 테스트 22 〉	통과 (28.09ms, 56.4MB)
// 테스트 23 〉	통과 (27.67ms, 56.5MB)
// 테스트 24 〉	통과 (29.14ms, 56.5MB)
// 테스트 25 〉	통과 (0.18ms, 33.5MB)
// 테스트 26 〉	통과 (0.18ms, 33.4MB)
// 테스트 27 〉	통과 (0.17ms, 33.4MB)
// 테스트 28 〉	통과 (19.35ms, 49.4MB)
// 테스트 29 〉	통과 (0.53ms, 34.2MB)
// 테스트 30 〉	통과 (14.23ms, 44.9MB)
