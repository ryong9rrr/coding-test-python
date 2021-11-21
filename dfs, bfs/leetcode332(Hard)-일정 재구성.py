# 큐와 dfs // 52ms (98.72%)
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(collections.deque)
        
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)
        
        route = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].popleft())
            route.append(node)
            
        dfs("JFK")
        
        return route[::-1]

# 큐, 스택, 반복문으로 처리 // 60ms (85.77%)
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(collections.deque)
        
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)
        
        route, stack = [], ["JFK"]
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            route.append(stack.pop())
                
        return route[::-1]
        