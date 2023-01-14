# itertools.product를 이용한 조합추출 // 16ms
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        combinations = list(itertools.product(*[phone[num] for num in digits]))
        return ["".join(tup) for tup in combinations]


# dfs
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        N = len(digits)
        result = []

        def dfs(index, path):
            if index == N:
                result.append(path)
                return
            for char in phone[digits[index]]:
                dfs(index + 1, path + char)

        dfs(0, "")

        return result