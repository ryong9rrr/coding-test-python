"""
1-1. 만약 mid의 인덱스가 홀수이고, (홀수 이기 때문에) nums[mid - 1] == nums[mid] 라면 mid를 기준으로 왼쪽의 숫자들은 페어가 맞다. 
  따라서 왼쪽 포인터를 mid + 1로 조정한다. (오른쪽 부분을 탐색)
1-2. 만약 mid의 인덱스가 짝수이고, (짝수이기 때문에) nums[mid] == nums[mid]면 mid를 기준으로 왼쪽의 숫자들은 페어가 맞다.
  따라서 왼쪽 포인터를 mid + 1로 조정한다. (오른쪽 부분을 탐색)
2. 그렇지 않다면 single number는 왼쪽 부분에 존재한다는 것이므로 right를 mid로 줄여준다.
"""
# 184ms(48.70%), 23.7MB(39.30%)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or \
                (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid

        
        return nums[left]