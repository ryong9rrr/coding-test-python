// 자바스크립트 - shift()를 사용했을 때
function solution(progresses, speeds) {
  const q = []
  for (let i = 0; i < speeds.length; i++) {
    q.push(Math.ceil((100 - progresses[i]) / speeds[i]))
  }
  let prev = q.shift()
  let result = [1]
  while (q.length > 0) {
    const current = q.shift()
    if (prev >= current) {
      result[result.length - 1]++
    } else {
      result.push(1)
      prev = current
    }
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 30MB)
// 테스트 2 〉	통과 (0.13ms, 30.3MB)
// 테스트 3 〉	통과 (0.09ms, 30.3MB)
// 테스트 4 〉	통과 (0.09ms, 30.4MB)
// 테스트 5 〉	통과 (0.09ms, 30.2MB)
// 테스트 6 〉	통과 (0.10ms, 30.4MB)
// 테스트 7 〉	통과 (0.16ms, 30.3MB)
// 테스트 8 〉	통과 (0.10ms, 30.2MB)
// 테스트 9 〉	통과 (0.09ms, 30.3MB)
// 테스트 10 〉	통과 (0.10ms, 30.2MB)
// 테스트 11 〉	통과 (0.08ms, 30.3MB)

// 스택을 큐처럼 사용했을 때
function solution(progresses, speeds) {
  const N = progresses.length
  const stack = []
  for (let i = 0; i < N; i++) {
    stack.push(Math.ceil((100 - progresses[i]) / speeds[i]))
  }
  stack.reverse() // 스택을 큐 처럼 사용하기 위해
  let prev = stack.pop()
  let result = [1]
  while (stack.length > 0) {
    const current = stack.pop()
    if (prev >= current) {
      result[result.length - 1]++
    } else {
      result.push(1)
      prev = current
    }
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 30.2MB)
// 테스트 2 〉	통과 (0.11ms, 30MB)
// 테스트 3 〉	통과 (0.12ms, 30.1MB)
// 테스트 4 〉	통과 (0.09ms, 30.1MB)
// 테스트 5 〉	통과 (0.07ms, 30.1MB)
// 테스트 6 〉	통과 (0.07ms, 30.1MB)
// 테스트 7 〉	통과 (0.11ms, 29.9MB)
// 테스트 8 〉	통과 (0.10ms, 30.2MB)
// 테스트 9 〉	통과 (0.09ms, 30.1MB)
// 테스트 10 〉	통과 (0.11ms, 30.1MB)
// 테스트 11 〉	통과 (0.06ms, 30.1MB)

// Queue 모듈을 구현했을 때 => 아무래도 스택처럼 푼 것보다는 시간이 더 걸릴수밖에 없음.
// 반드시 "큐"를 사용하여야 하는 문제에서만 써먹어보자.
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

function solution(progresses, speeds) {
  const N = progresses.length
  const q = new Queue()
  for (let i = 0; i < N; i++) {
    q.enqueue(Math.ceil((100 - progresses[i]) / speeds[i]))
  }

  const result = [1]
  let prev = q.dequeue()

  while (q.size > 0) {
    const current = q.dequeue()
    if (prev >= current) {
      result[result.length - 1]++
    } else {
      result.push(1)
      prev = current
    }
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.34ms, 30.2MB)
// 테스트 2 〉	통과 (0.20ms, 29.9MB)
// 테스트 3 〉	통과 (0.26ms, 30.1MB)
// 테스트 4 〉	통과 (0.18ms, 30.1MB)
// 테스트 5 〉	통과 (0.32ms, 30.2MB)
// 테스트 6 〉	통과 (0.15ms, 29.9MB)
// 테스트 7 〉	통과 (0.33ms, 30.1MB)
// 테스트 8 〉	통과 (0.18ms, 30.1MB)
// 테스트 9 〉	통과 (0.37ms, 29.9MB)
// 테스트 10 〉	통과 (0.34ms, 29.9MB)
// 테스트 11 〉	통과 (0.31ms, 30MB)
