# 492ms

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def solution(N, prevWinInfo, changedWinInfo):
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (N + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (N + 1) for _ in range(N + 1)]

    # 작년 순위로 그래프를 초기화
    for i in range(N):
        for j in range(i + 1, N):
            graph[prevWinInfo[i]][prevWinInfo[j]] = True
            indegree[prevWinInfo[j]] += 1

    # 변경된 순위대로 간선의 방향을 뒤집기
    for a, b in changedWinInfo:
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 알고리즘 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False # 그래프 내 사이클이 존재하는지 여부

    # 정확히 노드의 개수만큼 반복
    for i in range(N):
        # 큐가 비어있다면 사이클이 발생했다는 것
        if not q:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(1, N + 1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()

TEST_CASE = int(input())

for _ in range(TEST_CASE):
    N = int(input())
    prevWinInfo = list(map(int, input().split()))
    M = int(input())
    changedWinInfo = []
    for _ in range(M):
        changedWinInfo.append(list(map(int, input().split())))

    solution(N, prevWinInfo, changedWinInfo)