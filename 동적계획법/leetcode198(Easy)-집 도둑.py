# 책 풀이, OrderedDict 사용
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp.popitem()[1]

# 내 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            value = max(dp[i - 1], nums[i] + dp[i - 2])
            dp.append(value)
        return dp[-1]