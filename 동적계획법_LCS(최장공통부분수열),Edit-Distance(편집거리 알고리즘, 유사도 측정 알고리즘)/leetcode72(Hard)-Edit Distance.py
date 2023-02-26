# 재귀(시간초과) : 두 단어 중 길이가 긴 단어의 길이를 m이라고 할 때, 시간복잡도는 O(3^m)
class Solution:
    def recursive_min_distance(self, word1, word2, word1_index, word2_index):
        if word1_index == 0:
            return word2_index
        
        if word2_index == 0:
            return word1_index
        
        if word1[word1_index - 1] == word2[word2_index - 1]:
            return self.recursive_min_distance(word1, word2, word1_index - 1, word2_index - 1)
        
        insert_operation = self.recursive_min_distance(word1, word2, word1_index, word2_index - 1)
        delete_operation = self.recursive_min_distance(word1, word2, word1_index - 1, word2_index)
        replace_operation = self.recursive_min_distance(word1, word2, word1_index - 1, word2_index - 1)
        
        return min(insert_operation, delete_operation, replace_operation) + 1

    def minDistance(self, word1: str, word2: str) -> int:
        return self.recursive_min_distance(word1, word2, len(word1), len(word2))

# 타뷸레이션(바텀-업) DP : 165ms(66.43%), 17.6MB(29.79%)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # dp 테이블 초기화
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        # 최소 편집 거리 구하기
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    continue
                min_distance = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                dp[i][j] = 1 + min_distance
        
        return dp[-1][-1]