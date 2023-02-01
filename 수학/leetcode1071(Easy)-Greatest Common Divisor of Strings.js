// 76ms(62.50%) 41.9MB(90.63%)
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
  function GCD(a, b) {
    if (a % b === 0) return b
    return GCD(b, a % b)
  }

  if (str1 + str2 !== str2 + str1) {
    return ""
  }

  const length = GCD(str1.length, str2.length)
  return str2.slice(0, length)
}
