# 재귀로 문자열 분리 // 52ms
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 문자열 집합을 정렬하여 앞에서부터 차례대로 확인합니다.
        for char in sorted(set(s)):
            # 가장 처음 등장한 index부터 문자열을 잘라냅니다.
            suffix = s[s.index(char):]
            # 잘라낸 문자열의 집합과 원래 문자열의 집합이 같으면 첫 글자를 리턴하고 재귀적으로 호출합니다.
            if set(suffix) == set(s):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ""

# stack을 이용한 정석적인 풀이 // 32ms
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        seen = set()
        stack = []
        
        # 앞에서부터 한글자씩 확인합니다.
        for char in s:
            # 숫자를 하나씩 줄여줍니다.
            counter[char] -= 1
            # 이미 확인된 문자열이라면 넘어갑니다.
            if char in seen:
                continue
            # stack에 데이터가 있고,
            # 현재 확인하는 문자가 stack 맨위의 데이터보다 작고,
            # stack 맨 위의 데이터가 아직 뒤에 남아있다면
            # 스택에서 제거합니다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
