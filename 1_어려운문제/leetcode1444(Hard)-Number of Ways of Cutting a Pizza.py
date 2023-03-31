# 3차원 DP, 리트코드 풀이를 참고함...
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 1000000007
        rows = len(pizza)
        cols = len(pizza[0])

        # 사과테이블 초기화
        apples = [[0] * (cols + 1) for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                value = 1 if pizza[row][col] == "A" else 0
                cur = value + apples[row + 1][col] + apples[row][col + 1] - apples[row + 1][col + 1]
                apples[row][col] = cur
        
        # DP 테이블 초기화
        dp = collections.defaultdict(list)

        # 처음에는 모두 0으로 초기화
        for remain in range(k):
            dp[remain] = [[0] * cols for _ in range(rows)]

        # k가 0일 경우 앞에서 구한 사과테이블을 이용해서 초기화
        for row in range(rows):
            for col in range(cols):
                val = 1 if apples[row][col] > 0 else 0
                dp[0][row][col] = val

        # DP 시작
        for remain in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    for next_row in range(row + 1, rows):
                        if apples[row][col] > apples[next_row][col]:
                            val += dp[remain - 1][next_row][col]
                    for next_col in range(col + 1, cols):
                        if apples[row][col] > apples[row][next_col]:
                            val += dp[remain - 1][row][next_col]
                    dp[remain][row][col] = val % MOD
        
        return dp[k - 1][0][0]