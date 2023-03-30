# 접근 : 브루트포스 + 투포인터
# 43ms(9%), 13MB(31%)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = ti = 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1

        return si == len(s)