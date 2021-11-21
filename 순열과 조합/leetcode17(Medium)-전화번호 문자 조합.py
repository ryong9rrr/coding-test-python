# itertools.product를 이용한 조합추출 // 16ms
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        tempList = []
        for digit in digits:
            tempList.append(phone[digit])
        
        combination = list(itertools.product(*tempList))
        
        result = []
        for tuple in combination:
            result.append( "".join(tuple) )
            
        return result

# dfs로 조합추출 // 16ms
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            "1": "",
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
            
        # 예외처리
        if not digits:
            return []
        
        dfs(0, "")
        
        return result

# 보다 효율적인 풀이 // 16ms (78.13%)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if not digits:
            return []
        
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