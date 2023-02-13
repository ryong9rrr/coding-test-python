// 나의 풀이 : 59ms(93.15%), 41.7MB(62.14%)
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function (low, high) {
  const n = high - low + 1
  if (n % 2 === 0) {
    return n / 2
  }
  return low % 2 === 0 ? Math.floor(n / 2) : Math.floor(n / 2) + 1
}
