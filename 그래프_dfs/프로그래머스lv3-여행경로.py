# 리트코드332 - 일정 재구성 문제와 동일
from collections import defaultdict, deque
def solution(tickets):
    graph = defaultdict(deque)
    for v, w in sorted(tickets):
        graph[v].append(w)
    
    routes = []
    
    def dfs(v):
        while graph[v]:
            dfs(graph[v].popleft())
        routes.append(v)
        
    dfs("ICN")
    
    return routes[::-1]
    
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
"""

# 반복문과 스택으로 풀이
from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for v, w in tickets:
        graph[v].append(w)
    
    for v in graph.keys():
        graph[v].sort(reverse = True)
    
    stack = ["ICN"]
    result = []
    
    while stack:
        v = stack[-1]
        if graph[v]:
            stack.append(graph[v].pop())
        else:
            result.append(stack.pop())
    
    return result[::-1]
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
"""