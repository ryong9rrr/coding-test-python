// 브루트포스 + 투포인터
// 53ms(93%) 41MB(74%)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  let si = 0
  let ti = 0

  while (si < s.length && ti < t.length) {
    if (s[si] === t[ti]) {
      si += 1
    }
    ti += 1
  }

  return si === s.length
}
