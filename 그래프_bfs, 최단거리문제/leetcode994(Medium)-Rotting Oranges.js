// BFS : 75ms, 44.5MB
/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  const N = grid.length
  const M = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validateRange = (nx, ny) => {
    return 0 <= nx && nx < N && 0 <= ny && ny < M
  }

  const rottens = []
  let entireCount = 0
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < M; j += 1) {
      if (grid[i][j] !== 0) {
        entireCount += 1
        if (grid[i][j] === 2) {
          rottens.push([i, j, 0])
        }
      }
    }
  }

  let rottenCount = rottens.length
  let result = 0
  while (rottens.length > 0) {
    const [x, y, time] = rottens.shift()
    result = Math.max(result, time)
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validateRange(nx, ny) && grid[nx][ny] === 1) {
        rottenCount += 1
        grid[nx][ny] = 2
        rottens.push([nx, ny, time + 1])
      }
    }
  }

  return entireCount - rottenCount > 0 ? -1 : result
}
