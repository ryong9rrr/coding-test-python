class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_table = collections.defaultdict(int)
        for i, num in enumerate(nums2):
            index_table[num] = i

        def search(target_number, start_index):
            for i in range(start_index, len(nums2)):
                if nums2[i] > target_number:
                    return nums2[i]
            return -1

        ans = []
        for num in nums1:
            index = index_table[num]
            value  = search(num, index + 1)
            ans.append(value)
            
        return ans