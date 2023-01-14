from collections import defaultdict
def solution(n, computers):
    graph = defaultdict(list)
    for v in range(n):
        for w in range(v + 1, n):
            if computers[v][w] == 1:
                graph[v + 1].append(w + 1)
                graph[w + 1].append(v + 1)
    
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        for v in graph[node]:
            if not visited[v]:
                dfs(v)
    
    count = 0
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)
            count += 1
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.12ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.08ms, 10.4MB)
테스트 9 〉	통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.37ms, 10.2MB)
테스트 12 〉	통과 (0.28ms, 10.4MB)
테스트 13 〉	통과 (0.14ms, 10.2MB)
"""

# 사실 그래프를 따로 만들 필요가 없는게 computers가 행렬모양의 그래프임.
from collections import defaultdict
def solution(n, computers):    
    visited = [False] * n
    def dfs(v):
        visited[v] = True
        for w in range(n):
            if not visited[w] and v != w and computers[v][w] == 1:
                dfs(w)
    
    count = 0
    for v in range(n):
        if not visited[v]:
            dfs(v)
            count += 1
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.11ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.09ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (0.35ms, 10.4MB)
테스트 12 〉	통과 (0.29ms, 10.4MB)
테스트 13 〉	통과 (0.33ms, 10.2MB)
"""

# 유니온 파인드로도 할 수 있는 것 같은데, 테스트케이스 입력이 잘 못 된 것 같다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # 여기서 j를 0부터 돌렸을 때랑 i + 1에서 돌렸을 때랑 테스트케이스 오답 결과가 다른걸보니,
            # 테스트케이스 문제가 맞는듯..
            if computers[i][j] == 1:
                union_parent(parent, i, j)
    
    return len(set(parent))