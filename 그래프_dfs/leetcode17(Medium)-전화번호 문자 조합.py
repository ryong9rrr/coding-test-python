# itertools.product를 이용한 조합추출 // 16ms
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        temp = [dic[char] for char in digits]
        
        combinations = list(itertools.product(*temp))
        
        return ["".join(tup) for tup in combinations]

# dfs로 조합추출 // 16ms
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 예외처리
        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path + j)
        
        dfs(0, "")
        
        return result

# 보다 효율적인 풀이 // 16ms (78.13%)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            strings = dic[digits[index]]
            for s in strings:
                dfs(index + 1, path + s)
                
        dfs(0, "")
                
        return result