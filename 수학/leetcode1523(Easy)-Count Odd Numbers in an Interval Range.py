# 나의 풀이 : 30ms(76.46%), 13.9MB(50.4%)
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low + 1

        if n % 2 == 0:
            return n // 2

        return n // 2 + 1 if low % 2 == 1 else n // 2