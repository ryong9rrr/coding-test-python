# 212ms, 23.9MB
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1]
        post = [1]
        
        for num in nums:
            pre.append(pre[-1] * num)
            
        for num in nums[::-1]:
            post.append(post[-1] * num)
        
        pre.pop()
        post.pop()
        
        post = post[::-1]
        
        result = []
        
        for i in range(len(nums)):
            result.append(pre[i] * post[i])
            
        return result


# 메모리를 효율적으로 사용할 수 있음 // 208ms, 21MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]
        
        return out

"""js
var productExceptSelf = function(nums) {
    const out = [];
    let p = 1;
    for (let i = 0; i < nums.length; i++){
        out.push(p)
        p *= nums[i]
    }
    
    p = 1;
    for (let i = nums.length - 1; i > -1; i--){
        out[i] *= p;
        p *= nums[i]
    }
    
    return out
};
"""