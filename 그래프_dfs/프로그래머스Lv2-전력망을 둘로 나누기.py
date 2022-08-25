# dfs
from collections import defaultdict

def dfs(node, visited, graph):
    visited.append(node)
    if not graph[node]:
        return len(visited)
    for v in graph[node]:
        if v not in visited:
            dfs(v, visited, graph)
    return len(visited)


def solution(n, wires):
    # 그래프 초기화
    graph = defaultdict(list)
    for v, w in wires:
        graph[v].append(w)
        graph[w].append(v)

    result = int(1e9)
    
    for v, w in wires:
        graph[v].remove(w)
        graph[w].remove(v)

        count = dfs(1, [], graph)

        result = min(result, abs(n - (count * 2)))

        graph[v].append(w)
        graph[w].append(v)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (15.56ms, 10.2MB)
테스트 2 〉	통과 (14.84ms, 10.3MB)
테스트 3 〉	통과 (8.14ms, 10.3MB)
테스트 4 〉	통과 (11.95ms, 10.2MB)
테스트 5 〉	통과 (10.70ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.15ms, 10.2MB)
테스트 9 〉	통과 (0.12ms, 10.2MB)
테스트 10 〉	통과 (9.29ms, 10.2MB)
테스트 11 〉	통과 (10.74ms, 10.2MB)
테스트 12 〉	통과 (12.32ms, 10.2MB)
테스트 13 〉	통과 (8.48ms, 10.1MB)
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