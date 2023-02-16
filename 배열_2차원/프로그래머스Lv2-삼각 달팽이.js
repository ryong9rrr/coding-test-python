const fillMatrix = (headX, headY, number, width, matrix) => {
  const dx = [1, 0, -1]
  const dy = [0, 1, -1]
  let x = headX
  let y = headY

  matrix[x][y] = number++

  const fillAndMatrix = (direction) => {
    x += dx[direction]
    y += dy[direction]
    matrix[x][y] = number++
  }

  for (let i = 0; i < width - 1; i += 1) {
    fillAndMatrix(0)
  }

  for (let i = 0; i < width - 1; i += 1) {
    fillAndMatrix(1)
  }

  for (let i = 0; i < width - 2; i += 1) {
    fillAndMatrix(2)
  }

  return number
}

function solution(n) {
  const matrix = Array.from({ length: n }, () => new Array(n).fill(0))

  let number = 1
  let headX = 0
  let headY = 0
  let width = n
  while (width >= 1) {
    number = fillMatrix(headX, headY, number, width, matrix)
    headX += 2
    headY += 1
    width -= 3
  }

  const result = []
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < i + 1; j += 1) {
      result.push(matrix[i][j])
    }
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.15ms, 33.5MB)
// 테스트 2 〉	통과 (0.12ms, 33.6MB)
// 테스트 3 〉	통과 (0.18ms, 33.4MB)
// 테스트 4 〉	통과 (0.97ms, 37.5MB)
// 테스트 5 〉	통과 (1.08ms, 37.7MB)
// 테스트 6 〉	통과 (0.94ms, 37.5MB)
// 테스트 7 〉	통과 (37.44ms, 102MB)
// 테스트 8 〉	통과 (32.41ms, 108MB)
// 테스트 9 〉	통과 (29.96ms, 101MB)
