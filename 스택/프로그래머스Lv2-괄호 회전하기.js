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

  desc() {
    const arr = []
    let node = this.front
    while (node) {
      arr.push(node.value)
      node = node.next
    }
    return arr
  }
}

function isValid(s) {
  const stack = []
  for (const char of [...s]) {
    if (char === ']' || char === ')' || char === '}') {
      if (stack.length === 0) return false
      const top = stack[stack.length - 1]
      if (
        (top === '[' && char === ']') ||
        (top === '(' && char === ')') ||
        (top === '{' && char === '}')
      ) {
        stack.pop()
      } else {
        return false
      }
    } else {
      stack.push(char)
    }
  }
  return stack.length === 0
}

function solution(s) {
  const q = new Queue()
  ;[...s].forEach((v) => q.enqueue(v))

  let result = 0
  let n = s.length
  while (n--) {
    const string = q.desc().join('')
    if (isValid(string)) {
      result++
    }
    q.enqueue(q.dequeue())
  }
  return result
}
// 정확성 테스트
// 테스트 1 〉 통과 (38.21ms, 38.2MB)
// 테스트 2 〉 통과 (36.65ms, 38.2MB)
// 테스트 3 〉 통과 (36.73ms, 38.2MB)
// 테스트 4 〉 통과 (39.44ms, 38.3MB)
// 테스트 5 〉 통과 (39.98ms, 38.2MB)
// 테스트 6 〉 통과 (39.55ms, 38.2MB)
// 테스트 7 〉 통과 (38.82ms, 38.2MB)
// 테스트 8 〉 통과 (40.96ms, 38.3MB)
// 테스트 9 〉 통과 (42.45ms, 38.2MB)
// 테스트 10 〉 통과 (44.83ms, 38.2MB)
// 테스트 11 〉 통과 (50.50ms, 38.3MB)
// 테스트 12 〉 통과 (0.20ms, 33.5MB)
// 테스트 13 〉 통과 (0.21ms, 33.5MB)
// 테스트 14 〉 통과 (0.25ms, 33.5MB)

// Queue 구현없이 그냥 unshift
function isValid(s) {
  const stack = []
  for (const char of [...s]) {
    if (char === ']' || char === ')' || char === '}') {
      if (stack.length === 0) return false
      const top = stack[stack.length - 1]
      if (
        (top === '[' && char === ']') ||
        (top === '(' && char === ')') ||
        (top === '{' && char === '}')
      ) {
        stack.pop()
      } else {
        return false
      }
    } else {
      stack.push(char)
    }
  }
  return stack.length === 0
}

function solution(s) {
  const q = [...s]

  let result = 0
  let n = s.length
  while (n--) {
    const string = q.join('')
    if (isValid(string)) {
      result++
    }
    q.unshift(q.pop())
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (32.42ms, 37.7MB)
// 테스트 2 〉	통과 (28.52ms, 37.3MB)
// 테스트 3 〉	통과 (29.31ms, 37.4MB)
// 테스트 4 〉	통과 (28.04ms, 37.4MB)
// 테스트 5 〉	통과 (30.25ms, 37.6MB)
// 테스트 6 〉	통과 (27.76ms, 37.4MB)
// 테스트 7 〉	통과 (30.32ms, 37.5MB)
// 테스트 8 〉	통과 (40.31ms, 37.4MB)
// 테스트 9 〉	통과 (35.05ms, 37.5MB)
// 테스트 10 〉	통과 (65.90ms, 37.5MB)
// 테스트 11 〉	통과 (42.95ms, 37.4MB)
// 테스트 12 〉	통과 (0.08ms, 33.6MB)
// 테스트 13 〉	통과 (0.09ms, 33.4MB)
// 테스트 14 〉	통과 (0.11ms, 33.5MB)

// table 만들어서 풀기
function isValid(s) {
  const stack = []
  const table = {
    ')': '(',
    '}': '{',
    ']': '[',
  }
  for (const bracket of [...s]) {
    if (!(bracket in table)) {
      stack.push(bracket)
    } else if (stack.length === 0 || table[bracket] !== stack.pop()) {
      return false
    }
  }
  return stack.length === 0
}

function solution(s) {
  const q = [...s]

  let result = 0
  let n = s.length
  while (n--) {
    const string = q.join('')
    if (isValid(string)) {
      result++
    }
    q.unshift(q.pop())
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (47.60ms, 37.5MB)
// 테스트 2 〉	통과 (26.77ms, 37.3MB)
// 테스트 3 〉	통과 (27.15ms, 37.6MB)
// 테스트 4 〉	통과 (29.97ms, 37.4MB)
// 테스트 5 〉	통과 (31.75ms, 37.5MB)
// 테스트 6 〉	통과 (27.70ms, 37.4MB)
// 테스트 7 〉	통과 (30.50ms, 37.5MB)
// 테스트 8 〉	통과 (29.83ms, 37.4MB)
// 테스트 9 〉	통과 (37.34ms, 37.4MB)
// 테스트 10 〉	통과 (37.50ms, 37.5MB)
// 테스트 11 〉	통과 (42.74ms, 37.5MB)
// 테스트 12 〉	통과 (0.08ms, 33.4MB)
// 테스트 13 〉	통과 (0.09ms, 33.5MB)
// 테스트 14 〉	통과 (0.09ms, 33.5MB)
