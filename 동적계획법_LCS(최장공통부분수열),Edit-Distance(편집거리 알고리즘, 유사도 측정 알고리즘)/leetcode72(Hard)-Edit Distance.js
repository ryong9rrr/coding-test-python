// 타뷸레이션 DP : 83ms(87.10%), 47.3MB(42.20%)
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
  const n = word1.length
  const m = word2.length

  dp = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0))
  for (let i = 1; i < n + 1; i += 1) {
    dp[i][0] = i
  }
  for (let j = 1; j < m + 1; j += 1) {
    dp[0][j] = j
  }

  for (let i = 1; i < n + 1; i += 1) {
    for (let j = 1; j < m + 1; j += 1) {
      if (word1[i - 1] === word2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1]
        continue
      }
      const minDist = Math.min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
      dp[i][j] = minDist + 1
    }
  }

  return dp[n][m]
}
