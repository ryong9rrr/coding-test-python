// 크기가 동일한 n x m 행렬 더하기
const sumMatrix = (arr1, arr2) => {
  const n = arr1.length
  const m = arr1[0].length

  const result = []
  for (let i = 0; i < n; i++) {
    const temp = []
    for (let j = 0; j < m; j++) {
      const x = arr1[i][j]
      const y = arr2[i][j]
      temp.push(x + y)
    }
    result.push(temp)
  }
  return result
}

// N x M 행렬을 만드는 함수
function makeMatrix(N, M, defaultValue = 0) {
  const matrix = []
  for (let i = 0; i < N; i++) {
    const row = []
    for (let j = 0; j < M; j++) {
      row.push(defaultValue)
    }
    matrix.push(row)
  }
  return matrix
}

// N x N 행렬을 오른쪽으로 90도 회전하는 함수
function rotateMatrix90(matrix) {
  const N = matrix.length
  const result = makeMatrix(N, N, 0)
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      result[j][N - i - 1] = matrix[i][j]
    }
  }
  return result
}
