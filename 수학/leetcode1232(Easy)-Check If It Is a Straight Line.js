// 기울기 구하기
/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function (coordinates) {
  const calculateInc = (a, b) => {
    const [x1, y1] = a
    const [x2, y2] = b
    const dy = y1 - y2
    const dx = x1 - x2
    if (dy === 0) {
      return Infinity
    }
    if (dx === 0) {
      return -Infinity
    }
    return dy / dx
  }

  const inc = calculateInc(coordinates[0], coordinates[1])
  for (let i = 0; i < coordinates.length - 1; i += 1) {
    if (inc !== calculateInc(coordinates[i], coordinates[i + 1])) {
      return false
    }
  }
  return true
}
