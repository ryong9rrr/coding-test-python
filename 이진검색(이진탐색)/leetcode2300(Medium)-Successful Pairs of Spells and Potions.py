# 1681ms(64.59%), 39.5MB(11.5%)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        dp = {}
        potions.sort()

        def search(co):
            left, right = 0, len(potions) - 1
            while left < right:
                mid = left + ((right - left) // 2)
                num = potions[mid] * co
                if num < success:
                    left = mid + 1
                else:
                    right = mid
            return left

        ans = []
        for spell in spells:
            if spell not in dp:
                index = search(spell)
                pairs_count = 0 if potions[index] * spell < success else len(potions) - index
                ans.append(pairs_count)
                dp[spell] = pairs_count
                continue
            ans.append(dp[spell])
        return ans