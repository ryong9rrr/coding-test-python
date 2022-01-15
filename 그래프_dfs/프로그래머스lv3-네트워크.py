from collections import defaultdict
# 인접행렬리스트를 딕셔너리 형태로 변환하는 함수
def listToDict(matrix):
    n = len(matrix)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            # i != j을 하는 이유는 모든 노드가 자기 자신과 연결되어있기 때문에
            if i != j and matrix[i][j]:
                graph[i + 1].append(j + 1)
    return graph

def solution(n, computers):
    graph = listToDict(computers)
    visited = [False] * (n + 1)
    
    def dfs(v):
        # 연결되어있는 노드가 없거나 이미 방문한 노드라면
        if not v or visited[v]:
            return 1
        visited[v] = True
        for node in graph[v]:
            dfs(node)
        return 1
    
    count = 0
    for v in range(1, n + 1):
        if not visited[v]:
            count += dfs(v)
    return count

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.44ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.15ms, 10.3MB)
테스트 9 〉	통과 (0.10ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.2MB)
테스트 11 〉	통과 (0.68ms, 10.4MB)
테스트 12 〉	통과 (1.12ms, 10.2MB)
테스트 13 〉	통과 (0.48ms, 10.2MB)
"""