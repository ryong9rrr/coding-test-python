# dfs
from collections import defaultdict

def make_graph(wires):
    graph = defaultdict(set)
    for v, w in wires:
        graph[v].add(w)
        graph[w].add(v)
    return graph

def dfs(node, visited, graph):
    visited.append(node)
    if not graph[node]:
        return len(visited)
    for v in list(graph[node]):
        if v not in visited:
            dfs(v, visited, graph)
    return len(visited)

def solution(n, wires):
    graph = make_graph(wires)
    
    result = n
    for v, w in wires:
        graph[v].remove(w)
        graph[w].remove(v)
        
        count = dfs(1, [], graph)
        result = min(result, abs(n - count * 2))
        
        graph[v].add(w)
        graph[w].add(v)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (14.89ms, 10.4MB)
테스트 2 〉	통과 (9.80ms, 10.3MB)
테스트 3 〉	통과 (16.04ms, 10.2MB)
테스트 4 〉	통과 (10.00ms, 10.2MB)
테스트 5 〉	통과 (11.35ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.31ms, 10.2MB)
테스트 9 〉	통과 (0.15ms, 10.2MB)
테스트 10 〉	통과 (11.19ms, 10.3MB)
테스트 11 〉	통과 (12.09ms, 10.2MB)
테스트 12 〉	통과 (9.94ms, 10.2MB)
테스트 13 〉	통과 (9.55ms, 10.2MB)
"""


# 유니온파인드
uf = []

def find(a):
    global uf
    if uf[a] < 0: 
        return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: 
        return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    
    result = int(1e9)
    N = len(wires)
    
    for i in range(N):
        uf = [-1 for _ in range(n + 1)]
        graph = [wires[x] for x in range(N) if x != i]
        
        for v, w in graph: 
            merge(v, w)
            
        a, b = [x for x in uf[1:] if x < 0]
        
        result = min(result, abs(a - b))

    return result
"""
정확성  테스트
테스트 1 〉	통과 (7.26ms, 10.3MB)
테스트 2 〉	통과 (5.73ms, 10.3MB)
테스트 3 〉	통과 (4.54ms, 10.4MB)
테스트 4 〉	통과 (4.37ms, 10.4MB)
테스트 5 〉	통과 (5.78ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.28ms, 10.2MB)
테스트 9 〉	통과 (0.21ms, 10.3MB)
테스트 10 〉	통과 (5.32ms, 10.2MB)
테스트 11 〉	통과 (6.35ms, 10.2MB)
테스트 12 〉	통과 (5.45ms, 10.2MB)
테스트 13 〉	통과 (5.16ms, 10.2MB)
"""