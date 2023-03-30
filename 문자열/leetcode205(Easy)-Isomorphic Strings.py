# 46ms(50%), 14MB(12%)
class Solution:
    def indexing(self, string):
        table = {}
        for index, char in enumerate(string):
            if char not in table:
                table[char] = index
        return [table[char] for char in string]

    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        ss = self.indexing(s)
        tt = self.indexing(t)
        for i in range(n):
            if ss[i] != tt[i]:
                return False

        return True