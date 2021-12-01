"""
프로그래머스, 백준에도 있는 동일한 문제
"""

# functools로 풀기
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a, b):
            return -1 if int(str(a) + str(b)) < int(str(b) + str(a)) else 1
        
        result = sorted(nums, key = functools.cmp_to_key(compare), reverse=True)
        
        return str(int("".join(map(str, result))))  

# 삽입정렬로 풀기
class Solution(object):
    
    @staticmethod
    def to_swap(a, b):
        return str(a) + str(b) < str(b) + str(a)
    
    def largestNumber(self, nums):
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
        
        return str(int("".join(map(str, nums))))  