// 참고로 만약 이 문제가 코딩 인터뷰로 나온다면, 아래 풀이를 기대할 가능성이 크다.
// O(N)의 시간복잡도와 O(1)의 공간복잡도로 최적화한 풀이가 존재하는데, 이 풀이는 떠올리기가 어렵다.
// 최적화된 풀이는 리트코드 솔루션 2에서 제공하고 있다.

// 나의 풀이(리트코드 솔루션 1 - "구현" 풀이와 거의 동일) : 198ms(21.73%), 64.3MB(9.61%)
// 시간복잡도 : O(numRows * s의 길이)
const fillMatrix = (matrix, limit) => {
  const n = matrix.length
  const dx = [1, -1]
  const dy = [0, 1]

  let x = 0
  let y = 0
  let direction = 0
  let i = 0

  while (i < limit) {
    matrix[x][y] = i
    i += 1

    const nx = x + dx[direction]
    const ny = y + dy[direction]
    if (nx === n - 1) {
      direction = 1
    } else if (nx === 0) {
      direction = 0
    }
    x = nx
    y = ny
  }
}

const initializeMatrix = (numRows, limit) => {
  const numColumns = Math.ceil(limit / (2 * numRows - 2)) * (numRows - 1)
  return Array.from({ length: numRows }, () => new Array(numColumns).fill(null))
}

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1) {
    return s
  }

  const matrix = initializeMatrix(numRows, s.length)
  fillMatrix(matrix, s.length)

  let result = ""
  for (const row of matrix) {
    for (const value of row) {
      if (value !== null) {
        result += s[value]
      }
    }
  }
  return result
}
