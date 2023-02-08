const rotateBoard = (board) => {
  const N = board.length
  const M = board[0].length
  return Array.from({ length: M }, (v, j) => {
    const row = []
    for (let i = N - 1; i >= 0; i -= 1) {
      row.push(board[i][j])
    }
    return row
  })
}

function solution(m, n, board) {
  const matrix = rotateBoard(board)
  const di = [1, 0, 1]
  const dj = [0, 1, 1]

  const validate = (i, j) => {
    if (matrix[i][j] === "#") {
      return false
    }
    for (let k = 0; k < 3; k += 1) {
      const ni = i + di[k]
      const nj = j + dj[k]
      if (matrix[i][j] !== matrix[ni][nj]) {
        return false
      }
    }
    return true
  }

  const search = () => {
    const result = []
    for (let i = 0; i < n - 1; i += 1) {
      for (let j = 0; j < m - 1; j += 1) {
        if (validate(i, j)) {
          result.push([i, j])
        }
      }
    }
    return result
  }

  const remove = (targets) => {
    for (const [i, j] of targets) {
      matrix[i][j] =
        matrix[i + 1][j] =
        matrix[i][j + 1] =
        matrix[i + 1][j + 1] =
          "#"
    }
  }

  const rearrange = () => {
    for (let i = 0; i < n; i += 1) {
      matrix[i] = matrix[i].filter((v) => v !== "#")
      const rest = new Array(m - matrix[i].length).fill("#")
      matrix[i] = [...matrix[i], ...rest]
    }
  }

  const count = () => {
    return matrix.reduce(
      (counts, row) => counts + row.filter((v) => v === "#").length,
      0,
    )
  }

  while (true) {
    const targets = search()
    if (targets.length === 0) {
      return count()
    }
    remove(targets)
    rearrange()
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.46ms, 33.5MB)
// 테스트 2 〉	통과 (0.70ms, 33.5MB)
// 테스트 3 〉	통과 (0.55ms, 33.5MB)
// 테스트 4 〉	통과 (2.31ms, 34MB)
// 테스트 5 〉	통과 (14.20ms, 38.5MB)
// 테스트 6 〉	통과 (5.95ms, 37.9MB)
// 테스트 7 〉	통과 (1.03ms, 33.7MB)
// 테스트 8 〉	통과 (1.58ms, 33.9MB)
// 테스트 9 〉	통과 (0.42ms, 33.5MB)
// 테스트 10 〉	통과 (1.55ms, 33.6MB)
// 테스트 11 〉	통과 (2.28ms, 34MB)
