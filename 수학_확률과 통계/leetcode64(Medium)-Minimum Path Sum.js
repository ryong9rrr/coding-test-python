// 행렬 최단거리 문제(동적계획법) : 70ms(59%), 42MB(72%)
// 시간복잡도: O(N * M)
// 공간복잡도: O(1) - 여기서는 따로 DP행렬을 생성하지 않고 바로 원본 배열을 변형했기 때문.
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function (grid) {
  const n = grid.length
  const m = grid[0].length

  for (let i = 1; i < n; i += 1) {
    grid[i][0] += grid[i - 1][0]
  }

  for (let j = 1; j < m; j += 1) {
    grid[0][j] += grid[0][j - 1]
  }

  for (let i = 1; i < n; i += 1) {
    for (let j = 1; j < m; j += 1) {
      grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1])
    }
  }

  return grid[n - 1][m - 1]
}
