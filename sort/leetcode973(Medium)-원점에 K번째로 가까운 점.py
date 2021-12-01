# 정렬함수를 이용해서 풀기 // 540ms (93%)
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = sorted(points, key = lambda x : x[0]**2 + x[1]**2)
        
        return result[:k]

# 우선순위 큐(heapq)를 이용해서 풀기 // 600ms (60%)
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
            
        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        return result