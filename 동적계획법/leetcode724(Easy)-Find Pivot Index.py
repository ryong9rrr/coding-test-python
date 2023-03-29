"""
145ms(91%), 15.2MB(30%)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = []
        acc = 0
        for num in nums:
            acc += num
            sums.append(acc)

        maxSum = sums[-1]
        for i in range(len(nums)):
            left = sums[i] - nums[i]
            right = maxSum - sums[i]
            if left == right:
                return i

        return -1