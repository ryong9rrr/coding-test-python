# 다익스트라 문제
from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(list)
    # 양방향 그래프 구성
    for v, w in edge:
        graph[v].append(w)
        graph[w].append(v)
    
    # 노드에 방문했을 때의 최단거리를 담는다.
    visited = [0] * (n + 1)
    q = deque()
    q.append((1, 1)) #(v, distance)
    # bfs 시작
    while q:
        v, distance = q.popleft()
        if visited[v]:
            continue
        visited[v] += distance
        for w in graph[v]:
            # 방문하지 않은 노드만 방문(양방향 그래프라서)
            if not visited[w]:
                q.append((w, distance + 1))
    
    return visited.count(max(visited))

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.47ms, 10.3MB)
테스트 5 〉	통과 (1.78ms, 10.6MB)
테스트 6 〉	통과 (2.77ms, 11.2MB)
테스트 7 〉	통과 (26.76ms, 18.7MB)
테스트 8 〉	통과 (39.80ms, 20.9MB)
테스트 9 〉	통과 (47.83ms, 22.5MB)
"""