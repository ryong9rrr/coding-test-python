// 백트래킹 : 75ms, 45.3MB
/**
 * @param {string} tiles
 * @return {number}
 */
var numTilePossibilities = function (tiles) {
  const counter = [...tiles].reduce((obj, x) => {
    if (!obj[x]) obj[x] = 0
    obj[x]++
    return obj
  }, {})

  const dfs = (table) => {
    let result = 0
    for (const tile of Object.keys(table)) {
      if (table[tile] <= 0) {
        continue
      }
      table[tile] -= 1
      result += dfs(table) + 1
      table[tile] += 1
    }
    return result
  }

  return dfs(counter)
}
