// 65ms(75%), 44MB(26%)
/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  const counter = Array.from(s).reduce((obj, char) => {
    if (!obj[char]) obj[char] = 0
    obj[char] += 1
    return obj
  }, {})

  let ans = 0
  for (const [key, value] of Object.entries(counter)) {
    if (value % 2 === 0) {
      ans += value
      counter[key] = 0
    } else {
      if (value > 2) {
        ans += value - 1
        counter[key] = 1
      }
    }
  }

  for (const value of Object.values(counter)) {
    if (value === 1) {
      return ans + 1
    }
  }
  return ans
}
