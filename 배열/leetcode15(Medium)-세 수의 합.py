# 브루트포스 // 타임아웃
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        
        return result
"""js
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    const result = []
    
    for (let i = 0; i < nums.length - 2 ; i++){
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        for (let j = i + 1; j < nums.length - 1; j++){
            if (j > i + 1 && nums[j] === nums[j - 1]) continue;
            
            for (let k = j + 1; k < nums.length; k++){
                if (k > j + 1 && nums[k] === nums[k - 1]) continue;
                
                if (nums[i] + nums[j] + nums[k] === 0) {
                    result.push([nums[i], nums[j], nums[k]])
                }
            }
        }
    }
    return result
};
"""

# 투포인터 // 720ms
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
"""
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    const result = []
    
    for (let i = 0; i < nums.length - 2; i++){
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        let left = i + 1;
        let right = nums.length - 1;
        while (left < right){
            const _sum = nums[i] + nums[left] + nums[right];
            if (_sum < 0) left++;
            else if (_sum > 0) right--;
            else {
                result.push([nums[i], nums[left], nums[right]]);
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;
                left++;
                right--;
            }
        }
    }
    return result
};
"""