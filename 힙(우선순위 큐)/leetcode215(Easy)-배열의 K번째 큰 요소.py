"""
heapq 모듈의 heapify, nlargest..
"""

# 배열 요소들을 하나씩 꺼내어 heapq.heappush()로 최대힙 구성
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for n in nums:
            # heapq 모듈은 최소힙만 지원하기 때문에 최대힙 구성을 위해 음수로 표현
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap) 


# heapify로 바로 배열을 힙(최소힙)으로 구성
class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        # 최대힙 이므로
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

# nlargest로 가장 큰수 부터 k번째 까지 리스트를 반환, 맨 마지막 값이 답
class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]