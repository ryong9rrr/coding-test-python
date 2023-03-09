# 파라메트릭 서치 : 2146ms(55.94%), 28.8MB(6.68%)
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left = time[0]
        right = time[-1] * totalTrips

        def is_enough(mid):
            acc = 0
            for t in time:
                acc += (mid // t)
                if acc >= totalTrips:
                    return True
            return False
            

        while left < right:
            mid = int((right / 2) + (left / 2)) # avoid overflow
            if is_enough(mid):
                right = mid
            else:
                left = mid + 1

        return left