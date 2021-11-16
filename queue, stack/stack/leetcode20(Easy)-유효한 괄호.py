# stack과 table을 이용한 구현 // 16ms
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for bracket in s:
            if bracket not in table:
                stack.append(bracket)
            elif not stack or table[bracket] != stack.pop():
                return False
        return len(stack) == 0