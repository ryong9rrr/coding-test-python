// 접근 1 : 스택
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  const stack = []
  let maxProfit = 0

  for (let i = 0; i < prices.length; i += 1) {
    const price = prices[i]

    if (stack.length > 0 && prices[stack[stack.length - 1]] < price) {
      const minPrice = prices[stack[stack.length - 1]]
      maxProfit = Math.max(maxProfit, price - minPrice)
      continue
    }
    stack.push(i)
  }

  return maxProfit
}

// 접근 2 : DP(1)
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  const dp = [prices[0]]
  for (let i = 1; i < prices.length; i += 1) {
    dp.push(Math.min(dp[i - 1], prices[i]))
  }

  let maxProfit = 0
  for (let i = 0; i < prices.length; i += 1) {
    maxProfit = Math.max(maxProfit, prices[i] - dp[i])
  }
  return maxProfit
}

// 접근 3 : DP(2) - 카데인 알고리즘
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let maxProfit = 0
  let minPrice = Infinity

  for (const price of prices) {
    minPrice = Math.min(minPrice, price)
    maxProfit = Math.max(maxProfit, price - minPrice)
  }

  return maxProfit
}
