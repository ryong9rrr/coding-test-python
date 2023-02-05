// leetcode 567 문제와 동일한 문제임
// 딕셔너리 해시테이블 풀이 : 363ms(26.78%), 48.5MB(53.93%)
const lowerAlphabets = () => {
  return Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97))
}

const createAlphaMap = () => {
  return lowerAlphabets().reduce((obj, alpha) => {
    obj[alpha] = 0
    return obj
  }, {})
}

const isMatched = (aMap, bMap) => {
  for (const key of lowerAlphabets()) {
    if (aMap[key] !== bMap[key]) {
      return false
    }
  }
  return true
}

/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  if (p.length > s.length) {
    return []
  }

  const sMap = createAlphaMap()
  const pMap = createAlphaMap()

  for (let i = 0; i < p.length; i += 1) {
    sMap[s[i]] += 1
    pMap[p[i]] += 1
  }

  const result = []
  for (let i = 0; i < s.length - p.length; i += 1) {
    if (isMatched(sMap, pMap)) {
      result.push(i)
    }
    sMap[s[i]] -= 1
    sMap[s[i + p.length]] += 1
  }

  if (isMatched(sMap, pMap)) {
    result.push(s.length - p.length)
  }

  return result
}
