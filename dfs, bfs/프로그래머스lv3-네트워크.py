def solution(n, computers):
    # 인접행렬리스트를 딕셔너리형태 리스트로 변환
    def matrix_to_dic(matrix:list)->dict:
        graph = {}
        n = len(matrix)
        for i in range(n):
            graph[i + 1] = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] and i != j:
                    graph[i+1].append(j+1)
        return graph
    
    graph = matrix_to_dic(computers)
    
    count = 0
    visited = [False] * (n + 1)
    
    def dfs(node):
        #노드가 없다면
        if not node:
            return 1
        #이미 방문을 끝낸 노드라면
        if visited[node]:
            return 1
        visited[node] = True
        for v in graph[node]:
            dfs(v)
        return 1
    
    for i in range(1, n+1):
        if not visited[i]:
            count += dfs(i)
    
    return count

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.17ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.14ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.08ms, 10.2MB)
테스트 11 〉	통과 (0.52ms, 10.4MB)
테스트 12 〉	통과 (0.46ms, 10.3MB)
테스트 13 〉	통과 (0.22ms, 10.3MB)
"""