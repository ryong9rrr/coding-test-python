"""
접근 1 : 브루트포스
- 시간복잡도 : O(N^2)
- 공간복잡도 : O(1)
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        ans = 0
        for i in range(n):
            acc = 0
            co = 1
            for j in range(i, n):
                acc += (satisfaction[j] * co)
                co += 1
            ans = max(ans, acc)
        
        return ans
    

"""
접근 2 : 구간 합 DP
- 시간복잡도 : O(N)
- 공간복잡도 : O(N)
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)

        ans = 0
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] += sums[i - 1] + satisfaction[i - 1]

            if sums[i] < 0:
                break
            
            ans += sums[i]

        return ans