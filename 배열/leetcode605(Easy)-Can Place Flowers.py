"""
<나의 풀이>
접근 : 그리디 + 배열 문제
- 시간복잡도 : O(N)
- 공간복잡도 : O(1)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def can_plant(index):
            if flowerbed[index] == 1:
                return False

            if index == 0:
                if index + 1 >= len(flowerbed):
                    return True
                return flowerbed[index + 1] == 0
            
            if index == len(flowerbed) - 1:
                if index - 1 < 0:
                    return True
                return flowerbed[index - 1] == 0
            
            return flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if can_plant(i):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False
    

"""
굿 아이디어 : 범위를 3군데로 지정해주는 것이 귀찮을 수 있는데, 이렇게 맨 앞, 맨 뒤에 빈 값을 넣게되면 매우 심플하게 풀이가 가능.
"""
class Solution:
    def canPlant(self, index, arr):
        if arr[index] == 1:
            return False
        return arr[index - 1] == 0 and arr[index + 1] == 0

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        extended = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) + 1):
            if self.canPlant(i, extended):
                extended[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False