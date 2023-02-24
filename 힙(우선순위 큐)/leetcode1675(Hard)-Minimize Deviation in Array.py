# 최대 힙 풀이 : 774ms(89.55%), 22.6MB(44.78%)
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_value = float("-inf")
        for num in set(nums):
            x = -num
            if num % 2 == 1:
                x *= 2
            heapq.heappush(heap, x)
            min_value = max(min_value, x)
        
        min_value = min_value * -1
        deviation = float("inf")

        while True:
            max_value = heapq.heappop(heap) * -1
            deviation = min(deviation, max_value - min_value)
            if max_value % 2 == 1:
                break
            max_value //= 2
            min_value = min(min_value, max_value)
            heapq.heappush(heap, max_value * -1)

        return deviation