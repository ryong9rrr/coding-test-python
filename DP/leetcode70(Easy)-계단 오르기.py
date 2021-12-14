# 나의 풀이, 타뷸레이션 // 17ms
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
            
        return dp[n]

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