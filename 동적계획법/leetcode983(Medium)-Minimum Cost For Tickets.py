# 41ms(87%), 14MB(58%)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = max(days)
        dp = [0] * (max_day + 1)
        dayset = set(days)

        def f(day):
            if 1 <= day <= max_day:
                return dp[day]
            return 0

        for day in range(1, max_day + 1):
            if day in dayset:
                dp[day] = min( f(day - 1) + costs[0], f(day - 7) + costs[1], f(day - 30) + costs[2] )
            else:
                dp[day] = dp[day - 1]

        return dp[-1]
    

# 범위를 신경안쓰기 위해, **뒤에서부터** DP를 진행해가는 방법도 가능
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (365 + 30 + 1)

        for day in range(365, -1, -1):
            if not day in days:
                dp[day] = dp[day + 1]
                continue
            dp[day] = min(dp[day + 1] + costs[0], dp[day + 7] + costs[1], dp[day + 30] + costs[2])

        return dp[1]