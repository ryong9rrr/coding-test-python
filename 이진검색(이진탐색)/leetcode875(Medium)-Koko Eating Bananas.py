"""
이분탐색(파라메트릭 서치) 풀이
- 시간복잡도 : piles의 가장 큰 수를 N이라 할 때 O(logN)
- 공간복잡도 : O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def is_slow(mid):
            acc = 0
            for pile in piles:
                acc += math.ceil(pile / mid) # 예를들어 0.xx개를 먹을 수 있다면 1개를 먹은 것으로 봐야함.
                if acc > h:
                    return True
            return False
        
        while left < right:
            mid = left + (right - left) // 2 # avoid overflow
            if is_slow(mid):
                left = mid + 1 # 현재 속도가 느리니까 먹는 속도를 더 빠르게 만들어줘야함.
            else:
                right = mid
        
        return left