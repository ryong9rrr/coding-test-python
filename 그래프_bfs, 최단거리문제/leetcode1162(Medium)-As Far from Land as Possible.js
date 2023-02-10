// 접근 1 : BFS, 100ms(88.68%), 49.8MB(46.23%)
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
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function (grid) {
  const N = grid.length
  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validateRange = (nx, ny) => {
    return 0 <= nx && nx < N && 0 <= ny && ny < N
  }

  const visited = Array.from({ length: N }, () => new Array(N).fill(-1))
  const landsQ = new MyQueue()
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      if (grid[i][j] === 1) {
        landsQ.enqueue([i, j, 0])
        visited[i][j] = 0
      }
    }
  }

  while (landsQ.size > 0) {
    const [x, y, dist] = landsQ.dequeue()
    const nDist = dist + 1
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validateRange(nx, ny) && visited[nx][ny] === -1) {
        visited[nx][ny] = nDist
        landsQ.enqueue([nx, ny, nDist])
      }
    }
  }

  let result = 0
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      result = Math.max(result, visited[i][j])
    }
  }

  return result > 0 ? result : -1
}

// 접근 2 : DP, 84ms(96.23%), 46.6MB(96.23%)
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function (grid) {
  const N = grid.length
  const MAX_DISTANCE = N * 2 + 1
  const dp = Array.from({ length: N }, () => new Array(N).fill(MAX_DISTANCE))

  // update top, left => bottom, right direction
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < N; j += 1) {
      if (grid[i][j] === 1) {
        dp[i][j] = 0
        continue
      }
      const topDist = i > 0 ? dp[i - 1][j] + 1 : MAX_DISTANCE
      const leftDist = j > 0 ? dp[i][j - 1] + 1 : MAX_DISTANCE
      dp[i][j] = Math.min(dp[i][j], topDist, leftDist)
    }
  }

  let ans = 0
  // update bottom, right => top, left direction
  for (let i = N - 1; i >= 0; i -= 1) {
    for (let j = N - 1; j >= 0; j -= 1) {
      const bottomDist = i < N - 1 ? dp[i + 1][j] + 1 : MAX_DISTANCE
      const rightDist = j < N - 1 ? dp[i][j + 1] + 1 : MAX_DISTANCE
      dp[i][j] = Math.min(dp[i][j], bottomDist, rightDist)
      ans = Math.max(ans, dp[i][j])
    }
  }

  return ans === 0 || ans === MAX_DISTANCE ? -1 : ans
}
