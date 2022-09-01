// shift를 사용, maxes를 역으로 정렬시켜서 count를 인덱스로 사용한 풀이
function solution(priorities, location) {
  const q = priorities.map((prior, loc) => [loc, prior])
  const maxes = priorities.sort((a, b) => b - a)

  let count = 0
  while (q.length > 0) {
    const [loc, prior] = q.shift()
    const max = maxes[count]
    if (prior === max) {
      count++
      if (loc === location) {
        return count
      }
    } else {
      q.push([loc, prior])
    }
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.13ms, 30MB)
// 테스트 2 〉	통과 (0.32ms, 29.9MB)
// 테스트 3 〉	통과 (0.18ms, 30.1MB)
// 테스트 4 〉	통과 (0.12ms, 29.8MB)
// 테스트 5 〉	통과 (0.12ms, 30.1MB)
// 테스트 6 〉	통과 (0.15ms, 29.7MB)
// 테스트 7 〉	통과 (0.16ms, 30.1MB)
// 테스트 8 〉	통과 (0.25ms, 29.7MB)
// 테스트 9 〉	통과 (0.13ms, 29.9MB)
// 테스트 10 〉	통과 (0.17ms, 30MB)
// 테스트 11 〉	통과 (0.28ms, 29.8MB)
// 테스트 12 〉	통과 (0.12ms, 29.9MB)
// 테스트 13 〉	통과 (0.23ms, 30MB)
// 테스트 14 〉	통과 (0.13ms, 29.9MB)
// 테스트 15 〉	통과 (0.13ms, 30MB)
// 테스트 16 〉	통과 (0.14ms, 30MB)
// 테스트 17 〉	통과 (0.24ms, 30MB)
// 테스트 18 〉	통과 (0.11ms, 30.1MB)
// 테스트 19 〉	통과 (0.20ms, 30.1MB)
// 테스트 20 〉	통과 (0.17ms, 30.1MB)

// 큐를 구현한 풀이
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

function solution(priorities, location) {
  const q = new Queue()
  priorities.forEach((prior, i) => q.enqueue([i, prior]))
  const maxes = priorities.sort((a, b) => a - b)

  let count = 0
  while (q.size > 0) {
    const [loc, prior] = q.dequeue()
    if (prior === maxes[maxes.length - 1]) {
      count++
      maxes.pop()
      if (loc === location) {
        return count
      }
    } else {
      q.enqueue([loc, prior])
    }
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.27ms, 30.1MB)
// 테스트 2 〉	통과 (0.61ms, 30.1MB)
// 테스트 3 〉	통과 (0.40ms, 30MB)
// 테스트 4 〉	통과 (0.38ms, 30.2MB)
// 테스트 5 〉	통과 (0.37ms, 30MB)
// 테스트 6 〉	통과 (0.42ms, 30MB)
// 테스트 7 〉	통과 (0.46ms, 29.8MB)
// 테스트 8 〉	통과 (0.55ms, 30.1MB)
// 테스트 9 〉	통과 (0.23ms, 30.1MB)
// 테스트 10 〉	통과 (0.42ms, 29.9MB)
// 테스트 11 〉	통과 (0.56ms, 29.9MB)
// 테스트 12 〉	통과 (0.38ms, 29.8MB)
// 테스트 13 〉	통과 (0.49ms, 30.1MB)
// 테스트 14 〉	통과 (0.30ms, 29.9MB)
// 테스트 15 〉	통과 (0.34ms, 29.7MB)
// 테스트 16 〉	통과 (0.44ms, 30MB)
// 테스트 17 〉	통과 (0.67ms, 29.9MB)
// 테스트 18 〉	통과 (0.49ms, 30MB)
// 테스트 19 〉	통과 (0.39ms, 30.1MB)
// 테스트 20 〉	통과 (0.40ms, 30.1MB)
