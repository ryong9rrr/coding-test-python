"""
<나의 풀이 : 구간을 [start, end] 식으로 분리해서 그 차이만큼 등차수열의 합으로 구하는 방법..>
- 시간복잡도 : O(N)
- 공간복잡도 : O(N)
"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subs = []
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
                continue

            end = i + 1
            while end < len(nums) and nums[end] == 0:
                end += 1
            subs.append(end - i)

            i = end

        if not subs:
            return 0

        return sum([x * (x + 1) // 2 for x in subs])
    

"""
하지만 굳이 구간을 배열로 나타낼 필요가 없음.
- 시간복잡도 O(N)
- 공간복잡도 O(1)
"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = acc = 0
        
        for num in nums:
            if num == 0: 
                acc += 1
            else: 
                acc = 0
            ans += acc
            
        return ans