// 접근 1 : BFS, 162ms(80.68%), 52.1MB(58.8%)
class MyNode {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class MyQueue {
  constructor() {
    this.front = this.tail = null
    this.size = 0
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

/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
  const N = mat.length
  const M = mat[0].length
  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validateRange = (nx, ny) => {
    return 0 <= nx && nx < N && 0 <= ny && ny < M
  }

  const visited = Array.from({ length: N }, () => new Array(M).fill(-1))
  const q = new MyQueue()
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < M; j += 1) {
      if (mat[i][j] === 0) {
        visited[i][j] = 0
        q.enqueue([i, j, 0])
      }
    }
  }

  while (q.size > 0) {
    const [x, y, dist] = q.dequeue()
    const nDist = dist + 1
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validateRange(nx, ny) && visited[nx][ny] === -1) {
        visited[nx][ny] = nDist
        q.enqueue([nx, ny, nDist])
      }
    }
  }

  return visited
}

// 접근 2 : DP, 152ms(86.18%), 50.6MB(72.37%)
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
  const N = mat.length
  const M = mat[0].length
  const MAX_DISTANCE = N * M + 1
  const dp = Array.from({ length: N }, () => new Array(M).fill(MAX_DISTANCE))

  // top-left => bottom-right
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < M; j += 1) {
      if (mat[i][j] === 0) {
        dp[i][j] = 0
        continue
      }
      const top = i > 0 ? dp[i - 1][j] + 1 : MAX_DISTANCE
      const left = j > 0 ? dp[i][j - 1] + 1 : MAX_DISTANCE
      dp[i][j] = Math.min(dp[i][j], top, left)
    }
  }

  // bottom-right => top-left
  for (let i = N - 1; i >= 0; i -= 1) {
    for (let j = M - 1; j >= 0; j -= 1) {
      const bottom = i < N - 1 ? dp[i + 1][j] + 1 : MAX_DISTANCE
      const right = j < M - 1 ? dp[i][j + 1] + 1 : MAX_DISTANCE
      dp[i][j] = Math.min(dp[i][j], bottom, right)
    }
  }

  return dp
}
