# 디버그 콘솔 돌려보자... 근데 더 좋은 로직은 없을까? // 3216ms (5%)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                counter += collections.Counter()
            
            if not counter:
                break
            
            result += n - sub_count + 1
        
        return result