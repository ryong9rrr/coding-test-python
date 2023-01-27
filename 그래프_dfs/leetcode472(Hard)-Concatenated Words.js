// 160ms(98.11%), 53MB(94.34%)
/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function (words) {
  const table = new Set(words)

  const dfs = (word, count) => {
    if (count >= 2 && word.length === 0) {
      return true
    }
    for (let i = 1; i < word.length + 1; i++) {
      const substr = word.substring(0, i)
      if (table.has(substr)) {
        if (dfs(word.slice(i), count + 1)) {
          return true
        }
      }
    }
    return false
  }

  return words.filter((word) => dfs(word, 0))
}
