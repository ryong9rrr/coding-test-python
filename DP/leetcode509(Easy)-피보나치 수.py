# 가장 기본적인 형태(수의 범위가 30밖에 안되서 통과한듯) // 1000ms (18%)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)

# 메모이제이션 // 16ms(85%)
class Solution(object):
    
    dp = collections.defaultdict(int)
    
    def fib(self, n):
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        
        return self.dp[n]

# 타뷸레이션 // 16ms
class Solution(object):
    
    dp = collections.defaultdict(int)
    
    def fib(self, n):
        self.dp[0], self.dp[1] = 0, 1
        
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 2] + self.dp[i - 1]
        
        return self.dp[n]

# 두 변수만 이용하기 // 16ms
class Solution(object):
    def fib(self, n):
        x, y = 0, 1
        
        for i in range(n):
            x, y = y, x + y
        
        return x