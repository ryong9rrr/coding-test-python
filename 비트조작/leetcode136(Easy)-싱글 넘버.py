"""
비트연산의 속도는 매우 빠르다.

단 하나의 값만을 찾는 문제이므로
XOR(^)연산을 사용
"""
# XOR 연산 // 92ms(99%)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result