# 앞뒤만 비교한다 // 44ms(76%)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]
        return result

# 1. 약간의 변형
class Solution(object):
    def maxProfit(self, prices):
        result = 0
        for i in range(len(prices) - 1):
            p = prices[i + 1] - prices[i]
            if p > 0:
                result += p
        return result

# (1)은 파이썬 답게 한줄처리 가능
class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))