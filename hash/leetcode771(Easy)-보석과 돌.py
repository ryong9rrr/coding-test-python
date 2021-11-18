# Counter를 이용해서 간편하게 // 24ms
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = collections.Counter(stones)
        
        result = 0
        for char in jewels:
            result += counter[char]
            
        return result

# 리스트컴프리헨션 // 12ms
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        return sum([s in jewels for s in stones])