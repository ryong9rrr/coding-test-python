// 60ms, 41.5MB
/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function (n) {
  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const matrix = Array.from({ length: n }, () => new Array(n).fill(0))

  const fillMatrix = (x, y, number, direction) => {
    if (number > n * n) {
      return
    }
    matrix[x][y] = number
    const nx = x + dx[direction]
    const ny = y + dy[direction]
    if (nx < 0 || nx >= n || ny < 0 || ny >= n || matrix[nx][ny] > 0) {
      direction = (direction + 1) % 4
    }
    fillMatrix(x + dx[direction], y + dy[direction], number + 1, direction)
  }

  fillMatrix(0, 0, 1, 0)

  return matrix
}
