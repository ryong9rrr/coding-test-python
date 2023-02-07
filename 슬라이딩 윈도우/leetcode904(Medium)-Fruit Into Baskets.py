# 해시 방식의 슬라이딩 윈도우 : O(N), 973ms(70.47%), 20.1MB(80.52%)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        left = 0
        baskets = {}
        
        for right, fruit in enumerate(fruits):
            baskets[fruit] = baskets.get(fruit, 0) + 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1

            result = max(result, right - left + 1)
        
        return result