# 투포인터 // 720ms (브루트포스 타임아웃)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        result = []
    
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, n-1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                
                if _sum < 0:
                    left +=1
                elif _sum > 0:
                    right -=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left < right and nums[right]==nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return result