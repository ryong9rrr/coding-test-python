# O(n^2)의 정직하고 직관적인 풀이... // 시간초과
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = []
        for i in range(n):
            current = temperatures[i]
            result.append(0)
            for j in range(i+1, n):
                if current < temperatures[j]:
                    result[-1] = j - i
                    break
        
        return result

# stack을 이용한 풀이 // 1120ms
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer