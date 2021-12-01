class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_arr = sorted(intervals, key = lambda x: x[0])
        
        result = []
        
        for a, b in sorted_arr:
            if result and a <= result[-1][1]:
                result[-1][1] = max(result[-1][1], b)
            else:
                result += [a, b], # 콤마(,) 연산자
                # result += [[a, b]] 와 같음
                # result.append([a, b]) 와 같음
        
        return result