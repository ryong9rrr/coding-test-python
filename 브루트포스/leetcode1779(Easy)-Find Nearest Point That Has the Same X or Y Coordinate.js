/**
 * @param {number} x
 * @param {number} y
 * @param {number[][]} points
 * @return {number}
 */
var nearestValidPoint = function (x, y, points) {
  const valid = (px, py) => {
    return px === x || py === y
  }

  const mht = (px, py) => {
    return Math.abs(px - x) + Math.abs(py - y)
  }

  let minDist = Infinity
  const validPoints = []
  for (let index = 0; index < points.length; index += 1) {
    const [px, py] = points[index]
    if (!valid(px, py)) {
      continue
    }
    const dist = mht(px, py)
    validPoints.push([index, dist])
    minDist = Math.min(minDist, dist)
  }

  for (const [index, dist] of validPoints) {
    if (minDist === dist) {
      return index
    }
  }
  return -1
}
