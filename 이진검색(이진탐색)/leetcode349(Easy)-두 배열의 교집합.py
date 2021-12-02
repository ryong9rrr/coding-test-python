# 집합논리연산을 사용 // 24ms(97%)
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)

# 브루트포스 // 100ms (5%)
class Solution(object):
    def intersection(self, nums1, nums2):
        result = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result

# bisect모듈을 사용한 이진검색으로 일치여부 판별 // 28ms (89%)
class Solution(object):
    def intersection(self, nums1, nums2):
        result = set()
        nums2.sort()
        
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        return result

# 투포인터를 사용한 완전탐색 // 36ms(54%)
class Solution(object):
    def intersection(self, nums1, nums2):
        result = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result