// 스택 풀이 : 88ms(70.53%), 52.9Mb(5.81%)
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

// 카데인 알고리즘 : 106ms(20.37%), 51.1MB(95.49%)
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = Infinity
  let maxProfit = 0

  prices.forEach((price) => {
    minPrice = Math.min(minPrice, price)
    maxProfit = Math.max(maxProfit, price - minPrice)
  })

  return maxProfit
}
