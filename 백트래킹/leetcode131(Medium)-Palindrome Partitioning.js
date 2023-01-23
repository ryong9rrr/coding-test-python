// 백트래킹 : 284ms(60.85%), 63.5MB(64.95%)
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function (s) {
  const N = s.length
  const result = []

  const isPalindrome = (string) => {
    return string === [...string].reverse().join("")
  }

  const dfs = (start, array) => {
    if (start >= N) {
      result.push(array)
      return
    }

    for (let end = start; end < N; end++) {
      const substr = s.slice(start, end + 1)
      if (isPalindrome(substr)) {
        array.push(substr)
        dfs(end + 1, [...array])
        array.pop()
      }
    }
  }

  dfs(0, [])

  return result
}

// 백트래킹 + DP : 248ms(85.89%), 64.4MB(57.97%)
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function (s) {
  const N = s.length
  const result = []
  const dp = Array.from({ length: N }, () => new Array(N).fill(false))

  const dfs = (start, array) => {
    if (start >= N) {
      result.push(array)
      return
    }

    for (let end = start; end < N; end++) {
      if (s[start] === s[end] && (end - start <= 2 || dp[start + 1][end - 1])) {
        dp[start][end] = true
        array.push(s.slice(start, end + 1))
        dfs(end + 1, [...array])
        array.pop()
      }
    }
  }

  dfs(0, [])

  return result
}
