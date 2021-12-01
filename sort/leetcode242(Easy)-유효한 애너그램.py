#애너그램인지 유무를 판별하는 가장 좋은 방법은 문자열을 정렬시키는 것
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)