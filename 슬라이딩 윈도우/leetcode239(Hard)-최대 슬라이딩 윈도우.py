"""
내가 직접 떠올린 풀이..책의 브루트포스 풀이랑 똑같았음.
but 시간초과, 브루트포스로는 풀리지 않는다.
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i+k]))
            
        return result


# 큐를 이용하여 최댓값을 계속 갱신하는 풀이... 하지만 시간초과
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        results = []
        window = collections.deque()
        current_max = float("-inf")
        
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
            
            if current_max == float("-inf"):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            results.append(current_max)
            
            if current_max == window.popleft():
                current_max = float("-inf")
        
        return results

# 데크를 이용 // 1500ms (60~ 90%)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q, results = deque(), []
        
        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()
            
            # 큐가아닌 스택으로 구현해야 함.
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            q.append(i)
            
            if i+1 >= k:
                results.append(nums[q[0]])
                
        return results