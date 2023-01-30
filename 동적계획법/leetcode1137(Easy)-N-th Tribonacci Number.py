# 39ms(39.1%), 13.8MB(54.1%)
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            t = dp[i - 3] + dp[i - 2] + dp[i - 1]
            dp.append(t)
        return dp[n]