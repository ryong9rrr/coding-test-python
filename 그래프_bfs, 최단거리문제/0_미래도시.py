"""
플로이드와샬 문제

방문원이 1번 회사에서 출발하여 K번 회사를 거쳐 X번 회사로 가는 최소시간
갈 수 없다면 -1를 출력하라.
하나의 간선을 지나는 시간은 모두 1이고 양방향그래프이다.

입력형식
회사의 개수(n), 간선의 개수(m) // 회사번호는 1부터 시작한다.
회사번호, 회사번호 ...        // 이어져 있는 회사 간선정보
회사번호, 회사번호            // 마지막 줄에는 X, K가 주어진다.

5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
-> 3

4 2
1 3
2 4
3 4
-> -1
"""
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        if i == j:
            graph[i][j] = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = graph[1][k] + graph[k][x]

print(result) if result < INF else print(-1)