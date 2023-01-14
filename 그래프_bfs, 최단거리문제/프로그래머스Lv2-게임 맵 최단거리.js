function solution(maps) {
  const N = maps.length
  const M = maps[0].length

  const dx = [0, 1, 0, -1]
  const dy = [-1, 0, 1, 0]

  const q = [[0, 0, 1]]

  const validateRange = (nx, ny) => {
    return 0 <= nx && nx < N && 0 <= ny && ny < M
  }

  while (q.length > 0) {
    const [x, y, count] = q.shift()
    if (x === N - 1 && y === M - 1) {
      return count
    }
    maps[x][y] = 0
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validateRange(nx, ny) && maps[nx][ny] === 1) {
        maps[nx][ny] = 0 // 여기서 마킹을 해줌으로써 불필요한 연산을 덜어낸다. (최적화)
        q.push([nx, ny, count + 1])
      }
    }
  }

  return -1
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.25ms, 33.6MB)
// 테스트 2 〉	통과 (0.24ms, 33.5MB)
// 테스트 3 〉	통과 (0.24ms, 33.6MB)
// 테스트 4 〉	통과 (0.23ms, 33.6MB)
// 테스트 5 〉	통과 (0.24ms, 33.5MB)
// 테스트 6 〉	통과 (0.24ms, 33.7MB)
// 테스트 7 〉	통과 (0.26ms, 33.6MB)
// 테스트 8 〉	통과 (0.35ms, 33.5MB)
// 테스트 9 〉	통과 (0.25ms, 33.5MB)
// 테스트 10 〉	통과 (0.25ms, 33.7MB)
// 테스트 11 〉	통과 (0.37ms, 33.5MB)
// 테스트 12 〉	통과 (0.23ms, 33.7MB)
// 테스트 13 〉	통과 (0.23ms, 33.5MB)
// 테스트 14 〉	통과 (0.27ms, 33.7MB)
// 테스트 15 〉	통과 (0.23ms, 33.6MB)
// 테스트 16 〉	통과 (0.11ms, 33.7MB)
// 테스트 17 〉	통과 (0.25ms, 33.6MB)
// 테스트 18 〉	통과 (0.11ms, 33.6MB)
// 테스트 19 〉	통과 (0.10ms, 33.5MB)
// 테스트 20 〉	통과 (0.10ms, 33.4MB)
// 테스트 21 〉	통과 (0.10ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (38.74ms, 36.8MB)
// 테스트 2 〉	통과 (6.71ms, 36.5MB)
// 테스트 3 〉	통과 (27.23ms, 36.5MB)
// 테스트 4 〉	통과 (29.78ms, 36.6MB)

// Queue 구현
class MyNode {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class MyQueue {
  constructor() {
    this.size = 0
    this.front = this.tail = null
  }

  get peek() {
    if (!this.front || !this.tail) {
      return undefined
    }
    return this.front.value
  }

  enqueue(value) {
    const node = new MyNode(value)
    if (!this.front || !this.tail) {
      this.front = this.tail = node
    } else {
      this.tail = this.tail.next = node
    }
    this.size += 1
  }

  dequeue() {
    if (!this.front || !this.tail) {
      return undefined
    }
    const result = this.front.value
    this.front = this.front.next
    this.size -= 1
    return result
  }
}

function solution(maps) {
  const N = maps.length
  const M = maps[0].length

  const dx = [0, 1, 0, -1]
  const dy = [-1, 0, 1, 0]

  const q = new MyQueue()
  q.enqueue([0, 0, 1])

  const validateRange = (nx, ny) => {
    return 0 <= nx && nx < N && 0 <= ny && ny < M
  }

  while (q.size > 0) {
    const [x, y, count] = q.dequeue()
    if (x === N - 1 && y === M - 1) {
      return count
    }
    maps[x][y] = 0
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validateRange(nx, ny) && maps[nx][ny] === 1) {
        maps[nx][ny] = 0 // 여기서 마킹을 해줌으로써 불필요한 연산을 덜어낸다. (최적화)
        q.enqueue([nx, ny, count + 1])
      }
    }
  }

  return -1
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.38ms, 33.5MB)
// 테스트 2 〉	통과 (0.34ms, 33.5MB)
// 테스트 3 〉	통과 (0.53ms, 33.5MB)
// 테스트 4 〉	통과 (0.39ms, 33.5MB)
// 테스트 5 〉	통과 (0.48ms, 33.4MB)
// 테스트 6 〉	통과 (0.41ms, 33.5MB)
// 테스트 7 〉	통과 (0.39ms, 33.4MB)
// 테스트 8 〉	통과 (0.38ms, 33.6MB)
// 테스트 9 〉	통과 (0.38ms, 33.4MB)
// 테스트 10 〉	통과 (0.57ms, 33.5MB)
// 테스트 11 〉	통과 (0.38ms, 33.5MB)
// 테스트 12 〉	통과 (0.35ms, 33.5MB)
// 테스트 13 〉	통과 (0.39ms, 33.5MB)
// 테스트 14 〉	통과 (0.35ms, 33.6MB)
// 테스트 15 〉	통과 (0.35ms, 33.5MB)
// 테스트 16 〉	통과 (0.26ms, 33.6MB)
// 테스트 17 〉	통과 (0.42ms, 33.5MB)
// 테스트 18 〉	통과 (0.19ms, 33.4MB)
// 테스트 19 〉	통과 (0.19ms, 33.4MB)
// 테스트 20 〉	통과 (0.16ms, 33.4MB)
// 테스트 21 〉	통과 (0.18ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (14.42ms, 37.4MB)
// 테스트 2 〉	통과 (9.03ms, 37.1MB)
// 테스트 3 〉	통과 (11.16ms, 37.3MB)
// 테스트 4 〉	통과 (12.84ms, 37.4MB)
