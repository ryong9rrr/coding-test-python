/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  if (n === 0) {
    return true
  }

  const extended = [0, ...flowerbed, 0] // 굿 아이디어

  for (let i = 1; i < flowerbed.length + 1; i += 1) {
    if (extended[i] === 1) {
      continue
    }
    if (extended[i - 1] === 0 && extended[i + 1] === 0) {
      extended[i] = 1
      n -= 1
      if (n === 0) {
        return true
      }
    }
  }

  return false
}
