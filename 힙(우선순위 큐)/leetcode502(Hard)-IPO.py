# 1303ms(27.10%), 37MB(93.71%)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted([[capital[i], profits[i]] for i in range(n)])
        index = 0
        heap = []

        def insert_to_heap():
            nonlocal index
            while index < n:
                cost, profit = projects[index]
                if cost <= w:
                    heapq.heappush(heap, -profit)
                    index += 1
                else:
                    break

        insert_to_heap() # heap에 초기값 넣기

        while k and heap:
            negative_profit = heapq.heappop(heap)
            w += (-negative_profit)
            k -= 1
            insert_to_heap()


        return w