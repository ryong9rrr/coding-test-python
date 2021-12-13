"""
python count()를 이용한 브루트포스 // 시간초과
-> count 함수가 O(N)의 시간복잡도를 갖기 때문에 시간초과가 난 것으로 예상됨
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

# count() 함수를 그대로 사용하되, DP(메모이제이션) 풀이 // 144ms (56%)
class Solution(object):
    def majorityElement(self, nums):
        counts = collections.defaultdict(int) 
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num

#(나의 풀이) Counter 를 이용 // 144ms (56%)
class Solution(object):
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        # num is key
        for num, count in counts.items():
            if count > (len(nums) // 2):
                return num

"""
분할정복 풀이 // 224ms(10%)

문제에서 과반수를 넘는 엘리먼트는 반드시 존재한다고 했으므로
"비둘기집 원리"에 의해 분할된 리스트 중 무조건 최소 1번은 과반수 엘리먼트가
살아남아 병합될 수 있다.
"""
class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        
        # 조건이 참이면 1(True), 거짓이면 0(False)
        return [b, a][nums.count(a) > half]

"""
파이썬다운 방식 // 132ms (89%)

정렬시켰을 때, 중앙에는 무조건 과반수 이상의 값이 들어올 것이라는 판단
"""
class Solution(object):
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) // 2]