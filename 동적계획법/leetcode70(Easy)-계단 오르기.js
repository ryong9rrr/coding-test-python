// 타뷸레이션
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const dp = [1, 1];
  for (let i = 2; i < n + 1; i += 1) {
    const value = dp[i - 2] + dp[i - 1];
    dp.push(value);
  }
  return dp[n];
};
