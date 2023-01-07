# 타뷸레이션
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n + 1):
            value = dp[i - 2] + dp[i - 1]
            dp.append(value)
        return dp[-1]

# 메모이제이션
class Solution(object):
    
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.dp[n]

# 스왑 풀이
class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for i in range(n):
            x, y = y, x + y
        return x