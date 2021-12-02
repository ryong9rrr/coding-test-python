# 투포인터 O(N) // 44ms(85%)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while not left == right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return left + 1, right + 1

# 이진검색 O(NlogN) // 68ms(22%)
class Solution(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            
            #binary search
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1

"""
bisect 모듈 사용
"""
# bisect + 슬라이싱 // 시간초과
class Solution(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i+k+2

# bisect + 슬라이싱 최소화 // 시간초과
class Solution(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            #슬라이싱을 최소화 하기 위해 변수에 저장
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i+k+1] == expected:
                return k+1, i+k+2

# bisect 범위설정 + 슬라이싱 제거 // 48ms(64%)
class Solution(object):
    def twoSum(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1