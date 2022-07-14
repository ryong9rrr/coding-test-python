function solution(board, moves) {
  const LEN = board.length
  let newBoard = []
  let col = []
  for (let i = 0; i < LEN; i++) {
    for (let row = 0; row < LEN; row++) {
      if ([...board][row][i] !== 0) {
        col.push([...board][row][i])
      }
    }
    col.reverse()
    newBoard.push(col)
    col = []
  }

  let count = 0
  let basket = []

  for (const i in moves) {
    if (newBoard[moves[i] - 1].length !== 0) {
      basket.push(newBoard[moves[i] - 1].pop())
      if (basket.length >= 2) {
        if (basket[basket.length - 1] == basket[basket.length - 2]) {
          basket.pop()
          basket.pop()
          count += 2
        }
      }
    }
  }
  return count
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.15ms, 29.8MB)
// 테스트 2 〉	통과 (0.11ms, 29.8MB)
// 테스트 3 〉	통과 (0.15ms, 30.3MB)
// 테스트 4 〉	통과 (0.81ms, 30.5MB)
// 테스트 5 〉	통과 (0.15ms, 30.3MB)
// 테스트 6 〉	통과 (0.14ms, 30MB)
// 테스트 7 〉	통과 (0.13ms, 30.1MB)
// 테스트 8 〉	통과 (0.58ms, 30.3MB)
// 테스트 9 〉	통과 (0.22ms, 30.1MB)
// 테스트 10 〉	통과 (0.38ms, 30.5MB)
// 테스트 11 〉	통과 (0.72ms, 30.4MB)

// Queue 클래스 모듈을 이용한 풀이
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

function solution(board, moves) {
  const SIZE = board.length
  const matrix = Array.from({ length: SIZE }, (v) => new Queue())

  // matrix 초기화
  for (let y = 0; y < SIZE; y++) {
    for (let x = 0; x < SIZE; x++) {
      if (board[x][y]) {
        matrix[y].enqueue(board[x][y])
      }
    }
  }

  const basket = []
  let result = 0

  for (const col of moves) {
    const x = col - 1
    if (matrix[x].size) {
      const target = matrix[x].dequeue()
      const basketLen = basket.length
      const basketTailItem = basket[basketLen - 1]
      if (basketLen > 0 && basketTailItem === target) {
        basket.pop()
        result += 2
      } else {
        basket.push(target)
      }
    }
  }

  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.37ms, 29.8MB)
// 테스트 2 〉	통과 (0.39ms, 30MB)
// 테스트 3 〉	통과 (0.22ms, 30.1MB)
// 테스트 4 〉	통과 (0.82ms, 29.8MB)
// 테스트 5 〉	통과 (0.39ms, 29.9MB)
// 테스트 6 〉	통과 (0.43ms, 30.1MB)
// 테스트 7 〉	통과 (0.41ms, 29.9MB)
// 테스트 8 〉	통과 (0.53ms, 29.9MB)
// 테스트 9 〉	통과 (0.51ms, 30MB)
// 테스트 10 〉	통과 (0.52ms, 30MB)
// 테스트 11 〉	통과 (0.60ms, 30MB)
