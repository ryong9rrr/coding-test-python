# 29ms(90%), 13MB(53%)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(list(s))

        ans = 0
        # 일단 짝수개는 계속 더해줌
        for key, value in counter.items():
            # 짝수개라면 모두 더해주고, 남은 개수를 0으로 만듬
            if value % 2 == 0:
                ans += value
                counter[key] = 0
            else:
                # 3이상의 홀수개라면 
                if value > 2:
                    ans += value - 1
                    counter[key] = 1
        
        # 남은 개수가 1인 것중 하나만 더해줌
        for key, value in counter.items():
            if ans % 2 == 1:
                break
            if value == 1:
                ans += 1

        return ans