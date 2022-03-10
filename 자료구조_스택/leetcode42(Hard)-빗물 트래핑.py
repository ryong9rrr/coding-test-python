# 투 포인터 // 56ms
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
                
        return volume

"""js
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    if (height.length === 0) return 0
    
    let volume = 0;
    let left = 0;
    let right = height.length - 1;
    let left_max = height[left];
    let right_max = height[right];
    
    while (left < right){
        left_max = Math.max(left_max, height[left]);
        right_max = Math.max(right_max, height[right]);
        
        if (left_max <= right_max){
            volume += left_max - height[left];
            left++;
        }else {
            volume += right_max - height[right];
            right--;
        }
    }
    
    return volume;
};
"""


# stack // 52ms
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break
                    
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
                
            stack.append(i)
            
        return volume

"""js
var trap = function(height) {
    const stack = [];
    let volume = 0;
    
    for (let i = 0; i < height.length; i++){
        
        while (stack.length > 0 && height[i] > height[stack[stack.length - 1]]){
            const top = stack.pop();
            
            if (stack.length === 0) break;
            
            const distance = i - stack[stack.length - 1] - 1;
            const waters = Math.min(height[i], height[stack[stack.length - 1]]) - height[top];
            volume += distance * waters
        }
        stack.push(i)
    }
    
    return volume
};
"""