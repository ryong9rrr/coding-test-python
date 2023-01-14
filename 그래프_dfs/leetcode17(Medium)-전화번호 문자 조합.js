// 61ms, 41.9MB
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (digits.length === 0) {
    return []
  }

  const phone = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  }

  const N = digits.length
  const result = []

  const dfs = (index, path) => {
    if (index === N) {
      result.push(path)
      return
    }

    for (const char of phone[digits[index]]) {
      dfs(index + 1, path + char)
    }
  }

  dfs(0, "")
  return result
}
