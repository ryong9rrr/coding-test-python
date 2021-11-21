# itertools를 이용한 조합 // 68ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        numbers = [x for x in range(1, n+1)]
        
        combinations = itertools.combinations(numbers, k)
        
        return list(map(list, list(combinations)))

"""
숫자가 1부터 n까지라는 점을 이용하여 하나씩 증가시키며 dfs
592ms (53.41%)
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        
        def dfs(number, path):
            if len(path) == k:
                results.append(path)
                return
            for i in range(number, n + 1):
                dfs(i+1, path + [i])
        
        dfs(1, [])
        
        return results

# 책에나온 dfs // 588ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        
        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        
        dfs([], 1, k)
        
        return results