// 61ms(80.85%), 43MB(34%)
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function (days, costs) {
  const maxDay = Math.max(...days)
  const daySet = new Set(days)
  const dp = new Array(maxDay + 1).fill(0)

  const f = (day) => {
    return 0 <= day && day <= maxDay ? dp[day] : 0
  }

  const [a, b, c] = costs
  for (let day = 1; day < maxDay + 1; day += 1) {
    if (daySet.has(day)) {
      dp[day] = Math.min(f(day - 1) + a, f(day - 7) + b, f(day - 30) + c)
    } else {
      dp[day] = dp[day - 1]
    }
  }

  return dp[maxDay] // == dp[dp.length - 1]
}

// 범위 신경 안쓰려면 뒤에서부터 풀 수도 있음.
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function (days, costs) {
  const daySet = new Set(days)
  const dp = new Array(365 + 30 + 1).fill(0)

  const [a, b, c] = costs
  for (let day = 365; day >= 0; day -= 1) {
    if (daySet.has(day)) {
      dp[day] = Math.min(dp[day + 1] + a, dp[day + 7] + b, dp[day + 30] + c)
    } else {
      dp[day] = dp[day + 1]
    }
  }

  return dp[0]
}
