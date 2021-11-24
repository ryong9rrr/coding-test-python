# 다익스트라 문제
from collections import defaultdict, deque
def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    #노드에 처음 방문했을때의 거리(최단거리)를 담는다.
    visited = [0] * (n + 1)
    
    q = deque()
    # (node, distance)
    q.append((1,1))
    while q:
        node, distance = q.popleft()
        if visited[node]:
            continue
        visited[node] += distance
        for v in graph[node]:
            #최적화를 위해 이미 방문한 노드는 큐에 담지 않음
            if not visited[v]:
                q.append((v, distance + 1))
    #결국 visited에는 각 노드로 가는 거리가 담기게 됨.
    _max = max(visited)
    return visited.count(_max)

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