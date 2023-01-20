// 60ms(87.54%), 42.2MB
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  const result = []

  for (let line = 0; line < numRows; line++) {
    const row = new Array(line + 1).fill(1)
    if (line >= 2) {
      for (let i = 1; i < line; i++) {
        row[i] = result[line - 1][i - 1] + result[line - 1][i]
      }
    }
    result.push(row)
  }

  return result
}
