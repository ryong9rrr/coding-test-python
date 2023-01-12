# 브루트포스, 시간초과
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(0, len(nums) - k + 1):
            windows = nums[i:i+k]
            result.append(max(windows))
        return result


# 큐를 이용하여 최댓값을 계속 갱신하는 풀이, 시간초과
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

# 데크를 이용하고, 슬라이딩 윈도우에 인덱스를 담는다. // 1500ms (60~ 90%)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows = collections.deque()
        result = []
        
        for i in range(len(nums)):
            if windows and i - windows[0] == k:
                windows.popleft()
            
            # 큐가아닌 스택으로 구현해야 함.
            while windows and nums[windows[-1]] <= nums[i]:
                windows.pop()
            
            windows.append(i)
            
            if i + 1 >= k:
                result.append(nums[windows[0]])
                
        return result