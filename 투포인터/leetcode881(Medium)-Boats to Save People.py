# 그리디 + 투포인터, 프로그래머스Lv2-구명보트 문제와 동일한 문제
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1

        count = 0
        while left <= right:
            weight = people[left] + people[right]
            if weight <= limit:
                left += 1
            right -= 1
            count += 1
        
        return count