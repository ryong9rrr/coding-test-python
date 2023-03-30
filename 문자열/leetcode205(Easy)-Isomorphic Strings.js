// 79ms(48%), 45MB(20%)

const indexing = (string) => {
  const table = {}
  Array.from(string).forEach((char, index) => {
    if (!table[char]) {
      table[char] = index
    }
  })
  return Array.from(string).map((char) => table[char])
}

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  const n = s.length
  const ss = indexing(s)
  const tt = indexing(t)

  for (let i = 0; i < n; i += 1) {
    if (ss[i] !== tt[i]) {
      return false
    }
  }
  return true
}
