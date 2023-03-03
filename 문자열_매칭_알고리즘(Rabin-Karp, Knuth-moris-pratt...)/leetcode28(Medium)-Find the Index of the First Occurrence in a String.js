// 라빈-카프, KMP(커누스-모리스-프랫)로 나중에 풀어보면 좋을듯

// Approach 1 ) 슬라이딩 윈도우 (그냥 문자열 슬라이싱)
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  const n = haystack.length
  const m = needle.length

  if (n < m) {
    return -1
  }

  for (let i = 0; i < n; i += 1) {
    if (haystack.slice(i, i + m) === needle) {
      return i
    }
  }

  return -1
}
