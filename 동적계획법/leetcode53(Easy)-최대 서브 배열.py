class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            value = max(0, sums[i - 1]) + nums[i]
            sums.append(value)
        return max(sums)

# 카데인 알고리즘
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = -sys.maxsize
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum