var maxProfit = function (prices) {
  let profit = 0
  let min_price = Infinity

  for (const price of prices) {
    min_price = Math.min(min_price, price)
    profit = Math.max(profit, price - min_price)
  }

  return profit
}
