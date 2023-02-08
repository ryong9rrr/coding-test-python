// 크기가 동일한 n x m 행렬 더하기
const sumMatrix = (matrix1, matrix2) => {
  const n = matrix1.length
  const m = matrix1[0].length

  const result = []
  for (let i = 0; i < n; i++) {
    const temp = []
    for (let j = 0; j < m; j++) {
      const x = matrix1[i][j]
      const y = matrix2[i][j]
      temp.push(x + y)
    }
    result.push(temp)
  }
  return result
}

// 곱셈이 가능한 두 행렬 곱하기
const multiplyMatrix = (matrix1, matrix2) => {
  const multiply = (arr1, arr2) => {
    return arr1.reduce((total, value, i) => total + value * arr2[i], 0)
  }

  const getColumns = (matrix, j) => {
    return Array.from({ length: matrix.length }, (v, i) => i).map(
      (i) => matrix[i][j],
    )
  }

  const result = []
  for (let i = 0; i < matrix1.length; i += 1) {
    const row = []
    for (let j = 0; j < matrix2[0].length; j += 1) {
      row.push(multiply(matrix1[i], getColumns(matrix2, j)))
    }
    result.push(row)
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

// N x M 행렬을 오른쪽으로 90도 회전하는 함수
function rotateMatrix90_version2(matrix) {
  const N = matrix.length
  const M = matrix[0].length
  const result = []
  for (let j = 0; j < M; j += 1) {
    const row = []
    for (let i = N - 1; i >= 0; i -= 1) {
      row.push(matrix[i][j])
    }
    result.push(row)
  }
  return result
}
