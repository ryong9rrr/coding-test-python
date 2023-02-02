// 75ms(47.96%), 44.1MB(36.23%)
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function (words, order) {
  const freq = [...order].reduce((obj, char, i) => {
    obj[char] = i
    return obj
  }, {})

  for (let i = 0; i < words.length - 1; i += 1) {
    const curWord = words[i]
    const nextWord = words[i + 1]
    const minLength = Math.min(curWord.length, nextWord.length)

    for (let j = 0; j < minLength; j += 1) {
      const curChar = curWord[j]
      const nextChar = nextWord[j]

      if (freq[curChar] < freq[nextChar]) {
        break
      }

      if (freq[curChar] > freq[nextChar]) {
        return false
      }

      if (j === minLength - 1 && curWord.length > nextWord.length) {
        return false
      }
    }
  }

  return true
}
