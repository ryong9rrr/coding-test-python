# 우선순위, 최대 최소 -> heap사용 // 88ms
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        heap = []
        
        for key in counter:
            # python에서 최대힙으로 구현하려면 음수처리를 하는 것이 치트키
            heapq.heappush(heap, (-counter[key], key))
            
        result = []
        
        for _ in range(k):
            result.append( heapq.heappop(heap)[1] )
            
        return result

# 리스트 컴프리헨션 // 88ms
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        
        return [x[0] for x in counter.most_common(k)]

# zip() // 84ms
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        
        return list(zip(*counter.most_common(k)))[0]