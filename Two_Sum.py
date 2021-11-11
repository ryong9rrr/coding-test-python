"""
알고리즘별 시간복잡도 비교
"""
# 브루트포스 - O(N^2), 3560ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# O(N), 48ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        numbers = defaultdict(int)
        
        for i in range(0, n):
            numbers[nums[i]] = i + 1
            
        for i in range(0, n):
            m = target - nums[i]
            if numbers[m] and i != numbers[m]-1:
                return [i, numbers[m]-1]

# O(N), 44ms (dictionary에서 if ~ in 연산은 평균 O(1)의 시간복잡도)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        numbers = {}
        
        for i in range(0, n):
            m = target - nums[i]
            if m in numbers:
                return [numbers[m], i]
            else:
                numbers[nums[i]] = i