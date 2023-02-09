// 이건 사실 "집합"문제인데, 떠올리기가 매우 어려운 아이디어임.
// 373ms(100%), 69.3MB(100%)
const intersect = (setA, setB) => [...setA].filter((v) => setB.has(v))

/**
 * @param {string[]} ideas
 * @return {number}
 */
var distinctNames = function (ideas) {
  const sets = ideas.reduce((res, idea) => {
    const suffix = idea[0]
    if (!res[suffix]) {
      res[suffix] = new Set()
    }
    res[suffix].add(idea.slice(1))
    return res
  }, {})

  const suffixes = Object.keys(sets)
  const n = suffixes.length
  let answer = 0
  for (let i = 0; i < n - 1; i += 1) {
    for (let j = i; j < n; j += 1) {
      const setA = sets[suffixes[i]]
      const setB = sets[suffixes[j]]
      const intersectionLength = intersect(setA, setB).length

      answer +=
        2 *
        ([...setA].length - intersectionLength) *
        ([...setB].length - intersectionLength)
    }
  }

  return answer
}
