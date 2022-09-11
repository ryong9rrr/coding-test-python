from collections import deque, defaultdict
def solution(n, s, a, b, fares):
    INF = int(1e9)
    floyd = [list(INF for _ in range(n + 1)) for _ in range(n + 1)]
    for v, w, cost in fares:
        floyd[v][w] = cost
        floyd[w][v] = cost
    
    # 플로이드-와샬
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
    
    result = INF
    for i in range(1, n + 1):
        print(i, floyd[i][1:])
        result = min(result, floyd[i][s] + floyd[i][a] + floyd[i][b])
    return result

    # bfs를 위해 가까운 곳부터 정렬
    # graph = {}
    # for v in range(1, n + 1):
    #     graph[v] = sorted([[w, floyd[v][w]] for w in range(1, n + 1)], key = lambda x: x[1])

    #bfs
    # result = INF
    # visited = [False] * (n + 1)
    # q = deque()
    # q.append(s)
    # while q:
    #     node = q.popleft()
    #     if visited[node]:
    #         continue
    #     visited[node] = True
    #     direct = floyd[node][a] + floyd[node][b]
    #     result = min(result, direct)
    #     for next_node, cost in graph[node]:
    #         if visited[next_node] or node == next_node:
    #             continue
    #         q.append(next_node)
    #         result = min(result, floyd[next_node][a] + floyd[next_node][b])
    #         break
    
    # print(result)