# 플로이드 워셜, 	30840KB 744ms
import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    v, w, cost = map(int, input().split())
    # 간성 정보가 여러 개 일 수 있으므로 가장 짧은 것만 저장
    graph[v][w] = min(graph[v][w], cost)

# 자기 자신으로 향하는 비용은 0으로 초기화
for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min( graph[a][b], graph[a][k] + graph[k][b] )

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()