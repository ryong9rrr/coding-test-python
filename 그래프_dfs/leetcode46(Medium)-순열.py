# itertools를 이용한 순열 // 24ms
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 튜플형태로 리턴하지만 리트코드는 튜플도 정답처리
        return list(itertools.permutations(nums))

        # 튜플형태를 배열로 리턴해서 정확하게 요구된 답변으로 처리하려면
        return list(map(list, itertools.permutations(nums)))

# dfs로 순열생성 // 32ms
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                # copy.deepcopy(prev_elements)
                results.append(prev_elements[:])
            
            for e in elements:
                # copy.deepcopy(elements)
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        
        return results