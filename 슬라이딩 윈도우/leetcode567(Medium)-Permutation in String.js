// O(l1 + 26(l2 - l1))의 슬라이딩 윈도우 풀이 : 214ms(33.74%), 51.7MB(10.84%)
const asciiIter = () => {
  return Array.from({ length: 26 }, (v, i) => i + 97)
}

const createAlphaMap = () => {
  return asciiIter()
    .map((ascii) => String.fromCharCode(ascii))
    .reduce((obj, alpha) => {
      obj[alpha] = 0
      return obj
    }, {})
}

const isMatched = (s1map, s2map) => {
  for (const ascii of asciiIter()) {
    const key = String.fromCharCode(ascii)
    if (s1map[key] !== s2map[key]) {
      return false
    }
  }
  return true
}

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  const s1map = createAlphaMap()
  const s2map = createAlphaMap()

  for (let i = 0; i < s1.length; i += 1) {
    s1map[s1[i]] += 1
    s2map[s2[i]] += 1
  }

  for (let i = 0; i < s2.length - s1.length; i += 1) {
    if (isMatched(s1map, s2map)) {
      return true
    }
    s2map[s2[i]] -= 1
    s2map[s2[i + s1.length]] += 1
  }

  return isMatched(s1map, s2map)
}
