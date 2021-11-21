# dfs // 80ms
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        
        dfs(target, 0, [])
        
        return result

"""
재귀를 시작하기 전에 조건을 걸어주면 좀 더 시간이 단축될 수 있음
하지만 사전에 정렬을 시켜줘야함
36ms (98.54%)
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        
        result = []
        
        def dfs(csum, index, path):
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                if csum - candidates[i] < 0:
                    break
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        
        return result