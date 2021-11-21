# 조합 // 20ms
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combinations = [[]]
        n = len(nums)
        
        while n:
            for c in list(itertools.combinations(nums, n)):
                combinations.append(c)
            n -= 1
        
        return combinations

# dfs // 20ms
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(index, path):
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        
        return result