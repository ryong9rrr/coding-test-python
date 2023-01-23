# 백트래킹으로만 풀 경우 : O(n * 2^n) 706ms(53.40)%, 30.3MB(62.53%)
class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(start, array):
            if start >= len(s):
                result.append(array)
                return
                
            for end in range(start, len(s)):
                substr = s[start: end + 1]
                if self.is_palindrome(substr):
                    array.append(substr)
                    dfs(end + 1, array[:])
                    array.pop()

        dfs(0, [])

        return result

# 백트래킹 + DP로 최적화: O(n^2), 652ms(88.97%), 30.1MB(69.72%)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        
        result = []

        dp = [[False] * N for _ in range(N)]

        def dfs(start, array):
            nonlocal dp
            if start >= N:
                result.append(array)
                return

            for end in range(start, N):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    array.append(s[start : end + 1])
                    dfs(end + 1, array[:])
                    array.pop()

        dfs(0, [])

        return result