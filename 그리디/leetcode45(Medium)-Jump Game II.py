# 136ms(68.89%), 15.1MB(54.98%)
class Solution:
    def jump(self, nums: List[int]) -> int:
        answer = 0
        cur_far = cur_end = 0

        for index in range(len(nums) - 1):
            cur_far = max(cur_far, index + nums[index])

            if index == cur_end:
                answer += 1
                cur_end = cur_far

        return answer