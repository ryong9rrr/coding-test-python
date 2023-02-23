# 우선순위 큐로 insert // 76ms(81%)
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        
        return result