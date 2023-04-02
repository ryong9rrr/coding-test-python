# 접근 1 : 스택
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0
        
        # 스택의 top은 항상 가장 작은 값의 인덱스를 위치시킨다.
        for i, price in enumerate(prices):
            if stack and prices[stack[-1]] < price:
                min_price = prices[stack[-1]]
                max_profit = max(max_profit, price - min_price)
                continue
            stack.append(i)
        
        return max_profit
    
# 접근 2 : DP(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [prices[0]]
        for i in range(1, len(prices)):
            dp.append(min(dp[i - 1], prices[i]))

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - dp[i])
        return max_profit
    

# 접근 3 : DP(2) - 카데인 알고리즘
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = int(1e9)

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit