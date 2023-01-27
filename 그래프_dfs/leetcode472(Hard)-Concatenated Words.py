# 548ms(57.23%), 27.7 MB(47.98%)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        table = set(words)

        def dfs(word, count):
            if count >= 2 and len(word) == 0:
                return True
            for i in range(1, len(word) + 1):
                substr = word[0 : i]
                if substr in table:
                    if dfs(word[i::], count + 1):
                        return True
            return False

        return [word for word in words if dfs(word, 0)]