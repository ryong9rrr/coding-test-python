# 브루트포스 // 시간초과
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def contains(s_substr_lst, t_lst):
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True
        
        if not s or not t:
            return ""
        
        window_size = len(t)
        
        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left: left+size]
                if contains(list(s_substr), list(t)):
                    return s_substr
        
        return ""


# 투 포인터 // 126ms        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            # 일단 right를 늘려본다.
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            # 일단 right를 다 늘려서 필요한 문자들을 포함한 문자열이 되면
            if missing == 0:
                # left에서 필요없는 문자는 다 짜른다.
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # 이렇게 찾은 문자열이 아직 end 설정이 안되어있거나 새로 찾은 문자열이 기존에 찾은 문자열보다 짧거나 같다면
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
                    
        return s[start:end]


# Counter를 사용한 풀이 // 2400ms
class Solution(object):
    def minWindow(self, s, t):
        t_count = collections.Counter(t)
        current_count = collections.Counter()
        
        start, end = float("-inf"), float("inf")
        
        left = 0
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            current_count[char] += 1
            
            # AND연산 결과로 왼쪽 포인터 이동 판단
            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1
        
        return s[start:end] if end - start <= len(s) else ""