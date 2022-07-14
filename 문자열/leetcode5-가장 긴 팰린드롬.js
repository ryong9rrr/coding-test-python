/*
 * @param {string} s
 * @return {string}
 */

function max(...args) {
  return args.sort((a, b) => b.length - a.length)[0]
}

var longestPalindrome = function (s) {
  if (s.length < 2 || s === [...s].reverse().join('')) return s

  function expand(left, right) {
    while (left >= 0 && right < s.length && s[left] == s[right]) {
      left--
      right++
    }
    return s.slice(left + 1, right)
  }

  let result = ''

  for (let i = 0; i < s.length - 1; i++) {
    result = max(result, expand(i, i + 1), expand(i, i + 2))
  }
  return result
}
