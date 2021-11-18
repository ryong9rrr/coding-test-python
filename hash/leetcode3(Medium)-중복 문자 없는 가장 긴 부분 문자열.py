"""
나의 풀이

첫번째 문자부터 하나씩 보며 중복된 문자가 나오면 break
사실상 O(n^2)의 시간복잡도 // 724ms
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxstr = ""
        
        for i in range(n):
            current = ""
            p = i
            while p < n:
                if s[p] not in current:
                    current += s[p]
                else:
                    break
                if len(maxstr) < len(current):
                    maxstr = current
                p += 1
        
        return len(maxstr)

# 투포인터 + 딕셔너리로 O(N) // 36ms
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[char] = i
            
        return max_length