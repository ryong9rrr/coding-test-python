# 32비트, XOR연산
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 0b0000000000000000000000000000000
        return bin(n^M).count("1")

# 파이썬은 자동으로 처리해줌
class Solution(object):
    def hammingWeight(self, n):
        return bin(n^0).count("1")

# 근데 사실 XOR 0은 의미가 없음
class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count("1")

"""
정석적인 비트연산

1을 뺀 값과 AND 연산을 하게 되면 비트가 1씩 빠지게 됨
"""
class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count