# 인접 리스트 + 재귀 풀이
from collections import defaultdict
def solution(n, computers):
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j]:
                graph[i + 1].append(j + 1)
                graph[j + 1].append(i + 1)
    
    count = 0
    visited = [False] * (n + 1)
    
    def dfs(v):
        if visited[v]:
            return 0
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs(w)
        return 1
    
    for v in range(1, n + 1):
        if not visited[v]:
            count += dfs(v)
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.11ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.08ms, 10MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.1MB)
테스트 11 〉	통과 (0.31ms, 10.4MB)
테스트 12 〉	통과 (0.40ms, 10.3MB)
테스트 13 〉	통과 (0.14ms, 10.2MB)
"""

# 사실 그래프를 따로 만들 필요가 없는게 computers가 행렬모양의 그래프임.
# 인접 행렬 + 재귀 풀이
from collections import defaultdict
def solution(n, computers):
    count = 0
    visited = [False] * (n)
    
    def dfs(v):
        if visited[v]:
            return 0
        visited[v] = True
        for w in range(n):
            if v == w or visited[w]:
                continue
            if computers[v][w]:
                dfs(w)
        return 1
    
    for v in range(n):
        if not visited[v]:
            count += dfs(v)
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.13ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.18ms, 10.2MB)
테스트 9 〉	통과 (0.12ms, 10.1MB)
테스트 10 〉	통과 (0.16ms, 10.1MB)
테스트 11 〉	통과 (0.75ms, 10.2MB)
테스트 12 〉	통과 (0.55ms, 10.3MB)
테스트 13 〉	통과 (0.21ms, 10.2MB)
"""

# 인접행렬 + stack 풀이
def solution(n, computers):
    count = 0
    visited = [False] * n
    
    def dfs(node):
        stack = [node]
        while stack:
            v = stack.pop()
            visited[v] = True
            for w in range(n):
                if v == w or visited[w]:
                    continue
                if computers[v][w]:
                    stack.append(w)
    
    for v in range(n):
        if not visited[v]:
            dfs(v)
            count += 1
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10MB)
테스트 4 〉	통과 (0.05ms, 9.98MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.34ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.18ms, 10.3MB)
테스트 9 〉	통과 (0.10ms, 10MB)
테스트 10 〉	통과 (0.11ms, 10MB)
테스트 11 〉	통과 (1.43ms, 10.4MB)
테스트 12 〉	통과 (0.91ms, 10.2MB)
테스트 13 〉	통과 (0.35ms, 10.1MB)
"""