// 69ms(51.56%), 42MB(24.68%)
/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  const dp = [0, 1, 1]
  for (let i = 3; i < n + 1; i++) {
    const t = dp[i - 3] + dp[i - 2] + dp[i - 1]
    dp.push(t)
  }
  return dp[n]
}
