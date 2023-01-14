// 98ms, 45.5MB
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const N = grid.length
  const M = grid[0].length

  const isVisited = (i, j) => grid[i][j] !== "1"
  const validateRange = (i, j) => 0 <= i && i < N && 0 <= j && j < M

  const dfs = (i, j) => {
    if (!validateRange(i, j) || isVisited(i, j)) {
      return
    }
    grid[i][j] = "#"
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
  }

  let count = 0
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < M; j += 1) {
      if (!isVisited(i, j)) {
        dfs(i, j)
        count += 1
      }
    }
  }
  return count
}
