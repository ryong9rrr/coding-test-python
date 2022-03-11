# 정렬한 후 2씩 넘어가며 min() // 248ms
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i+1])
            
        return result

# 생각해보면 min을 할 필요가 없음 // 228ms
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
            
        return result

"""js
var arrayPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let result = 0;
    
    for (let i = 0; i < nums.length; i += 2) result += nums[i]
    
    return result
};
"""

# 파이써닉 // 220ms
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])