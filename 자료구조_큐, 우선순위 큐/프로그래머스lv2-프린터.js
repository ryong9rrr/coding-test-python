function solution(priorities, location) {
  const q = priorities.map((p, i) => [i, p])
  const maxes = priorities.sort((a, b) => a - b)

  let count = 0
  while (q.length > 0) {
    const [loc, p] = q.shift()
    if (p === maxes[maxes.length - 1]) {
      if (loc === location) {
        return count + 1
      }
      count += 1
      maxes.pop()
    }
    q.push([loc, p])
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.21ms, 33.5MB)
// 테스트 2 〉	통과 (0.57ms, 33.7MB)
// 테스트 3 〉	통과 (0.30ms, 33.4MB)
// 테스트 4 〉	통과 (0.28ms, 33.6MB)
// 테스트 5 〉	통과 (0.08ms, 33.5MB)
// 테스트 6 〉	통과 (0.24ms, 33.5MB)
// 테스트 7 〉	통과 (0.27ms, 33.5MB)
// 테스트 8 〉	통과 (0.61ms, 33.5MB)
// 테스트 9 〉	통과 (0.21ms, 33.5MB)
// 테스트 10 〉	통과 (0.26ms, 33.4MB)
// 테스트 11 〉	통과 (0.42ms, 33.5MB)
// 테스트 12 〉	통과 (0.19ms, 33.4MB)
// 테스트 13 〉	통과 (0.54ms, 33.5MB)
// 테스트 14 〉	통과 (0.11ms, 33.4MB)
// 테스트 15 〉	통과 (0.19ms, 33.4MB)
// 테스트 16 〉	통과 (0.30ms, 33.5MB)
// 테스트 17 〉	통과 (0.57ms, 33.5MB)
// 테스트 18 〉	통과 (0.18ms, 33.5MB)
// 테스트 19 〉	통과 (0.41ms, 33.5MB)
// 테스트 20 〉	통과 (0.30ms, 33.5MB)

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
  priorities.forEach((p, i) => {
    q.enqueue([i, p])
  })
  const maxes = priorities.sort((a, b) => a - b)

  let count = 0
  while (q.size > 0) {
    const [loc, p] = q.dequeue()
    if (p === maxes[maxes.length - 1]) {
      if (loc === location) {
        return count + 1
      }
      count += 1
      maxes.pop()
    }
    q.enqueue([loc, p])
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.55ms, 33.6MB)
// 테스트 2 〉	통과 (1.25ms, 33.6MB)
// 테스트 3 〉	통과 (0.39ms, 33.5MB)
// 테스트 4 〉	통과 (0.35ms, 33.5MB)
// 테스트 5 〉	통과 (0.16ms, 33.5MB)
// 테스트 6 〉	통과 (0.40ms, 33.5MB)
// 테스트 7 〉	통과 (0.38ms, 33.5MB)
// 테스트 8 〉	통과 (0.62ms, 33.8MB)
// 테스트 9 〉	통과 (0.35ms, 33.5MB)
// 테스트 10 〉	통과 (0.44ms, 33.6MB)
// 테스트 11 〉	통과 (0.59ms, 33.6MB)
// 테스트 12 〉	통과 (0.36ms, 33.5MB)
// 테스트 13 〉	통과 (0.58ms, 33.6MB)
// 테스트 14 〉	통과 (0.18ms, 33.5MB)
// 테스트 15 〉	통과 (0.26ms, 33.5MB)
// 테스트 16 〉	통과 (0.36ms, 33.5MB)
// 테스트 17 〉	통과 (0.56ms, 33.6MB)
// 테스트 18 〉	통과 (0.37ms, 33.5MB)
// 테스트 19 〉	통과 (0.52ms, 33.5MB)
// 테스트 20 〉	통과 (0.36ms, 33.5MB)
