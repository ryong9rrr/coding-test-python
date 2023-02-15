"""
https://school.programmers.co.kr/learn/courses/30/lessons/120885?language=python3
프로그래머스 Lv0 - 이진수 더하기 문제와 동일한 문제이지만 

프로그래머스 문제에서는 a, b의 길이가 최대 10이고
이 문제에서는 최대 10^4 라는 점이 다르다. 파이썬은 숫자 범위가 커서 풀이가 동일한데,
자바스크립트는 BigInt를 사용해야함.
"""

# 내장메서드 사용 : 38ms(53.43%), 14MB(18.45%)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    

# 이진수 덧셈 구현 : 47ms(20.7%), 13.9MB(63.5%)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a) if len(a) > len(b) else len(b)

        a = a.zfill(max_len)
        b = b.zfill(max_len)  #("0" * (max_len - len(b))) + b

        result = ""
        carry = 0
        for i in range(max_len - 1, -1, -1):
            bin_a = int(a[i])
            bin_b = int(b[i])
            x = bin_a ^ bin_b ^ carry
            result += str(x)
            carry = 1 if bin_a + bin_b + carry >= 2 else 0

        if carry:
            result += str(carry)

        return result[::-1]