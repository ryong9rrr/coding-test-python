# 나의 풀이 // 650 ~ 900ms (10%), 모든 풀이가 시간은 비슷함.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [nums[0]]
        
        for i in range(1, len(nums)):
            sums.append(max(nums[i], nums[i] + sums[i-1]))
        
        return max(sums)

# max함수를 사용하지 않고 분기문으로
class Solution(object):
    def maxSubArray(self, nums):
        sums = [nums[0]]
        
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        
        return max(sums)

# 추가 변수 없이
class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        
        return max(nums)

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