# 파라메트릭 서치 : 764ms(22.77%), 17.1MB(78.6%)
class Solution:    
    def day(self, capacity, weights):
        n = load = 0
        for weight in weights:
            if load + weight > capacity:
                n += 1
                load = 0
            load += weight
        if load > 0:
            n += 1
        return n
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = right = 0
        for weight in weights:
            left = max(left, weight)
            right += weight
        
        while left < right:
            mid = left + ((right - left) // 2)
            need_day = self.day(mid, weights)
            if need_day <= days:
                right = mid
            else:
                left = mid + 1

        return left
    
# 약간의 최적화 : 665ms(29.55%), 17.1MB(78.6%)
class Solution:    
    def feasible(self, capacity, weights, days):
        n = load = 0
        for weight in weights:
            if load + weight > capacity:
                n += 1
                load = 0
            load += weight
            if n > days:
                return False
        if load > 0:
            n += 1
        return n <= days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = right = 0
        for weight in weights:
            left = max(left, weight)
            right += weight
        
        while left < right:
            mid = left + ((right - left) // 2)
            if self.feasible(mid, weights, days):
                right = mid
            else:
                left = mid + 1

        return left