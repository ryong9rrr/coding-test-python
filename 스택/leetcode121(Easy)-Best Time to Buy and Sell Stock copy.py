# 스택 풀이 : 1035ms(76.19%), 25MB(82.91%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0

        for i, price in enumerate(prices):
            if stack and prices[stack[-1]] < price:
                min_price = prices[stack[-1]]
                max_profit = max(max_profit, price - min_price)
                continue
            stack.append(i)
        
        return max_profit
    
# dp식 카데인 알고리즘 1 : 1205ms(22.60%), 24.6MB(98.9%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_prices = [prices[0]]
        for i in range(1, n):
            min_price = min(min_prices[i - 1], prices[i])
            min_prices.append(min_price)

        result = 0
        for i in range(n):
            result = max(result, prices[i] - min_prices[i])

        return result
    
# 그런데 사실 이렇게도 가능 ... 카데인 알고리즘 2 : 1088ms(60.45%), 25.1MB(32.77%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit