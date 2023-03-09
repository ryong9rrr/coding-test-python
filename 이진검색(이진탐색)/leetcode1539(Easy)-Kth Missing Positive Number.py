# O(logN)의 이분탐색 : 56ms(55.94%), 14.1MB(44.77%)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] <= k + mid:
                left = mid + 1
            else:
                right = mid
        
        return left + k