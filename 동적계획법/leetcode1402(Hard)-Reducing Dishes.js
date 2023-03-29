// 구간 합 DP
/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function (satisfaction) {
  const n = satisfaction.length
  satisfaction = satisfaction.sort((a, b) => b - a)

  let ans = 0
  const sums = new Array(n + 1).fill(0)
  for (let i = 1; i < n + 1; i += 1) {
    sums[i] = sums[i - 1] + satisfaction[i - 1]

    if (sums[i] < 0) {
      break
    }

    ans += sums[i]
  }

  return ans
}
