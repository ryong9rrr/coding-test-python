# 이 문제는 GCD를 사용하라는 문제
# 나의 풀이 : 36ms(66.52%), 14MB(23.70%)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        set_a = set(str1)
        set_b = set(str2)

        if set_a ^ set_b:
            return ""

        length = math.gcd(len(str1), len(str2))
        result = str2[:length]

        if result * (len(str1) // length) == str1 and result * (len(str2) // length) == str2:
            return result
        return ""
    
# 스마트한 풀이 : 28ms(93.33%), 13.8MB(70.81%)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 두 문자를 각각 더했을 때 결과가 다르다면 반복되지 않는 경우라는 것
        if str1 + str2 != str2 + str1:
            return ""

        # 겹치는 문자의 길이는 무조건 두 문자의 길이의 최대공약수
        length = math.gcd(len(str1), len(str2))
        return str2[:length]