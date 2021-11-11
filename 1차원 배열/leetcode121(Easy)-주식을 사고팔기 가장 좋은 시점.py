# 처음 푼 브루트포스 // 타임아웃
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            sell = max(prices[i+1:])
            result = max(result, sell - buy)
            
        return result

# 일반적인 브루트포스 // 타임아웃
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_price = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_price = max( max_price, prices[j] - prices[i] )
                
        return max_price


# 카데인(Kadane's) 알고리즘 O(n) // 908ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit