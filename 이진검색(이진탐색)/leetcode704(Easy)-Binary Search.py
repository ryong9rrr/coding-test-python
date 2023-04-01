class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            num = nums[mid]
            if num < target:
                left = mid + 1
            else:
                right = mid
        
        return left if nums[left] == target else -1