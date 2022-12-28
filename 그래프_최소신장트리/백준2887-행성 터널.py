# 1304ms

import sys
input = lambda: sys.stdin.readline().rstrip()

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())

# 부모 테이블 초기화
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

# (좌표, 행성의 번호) 형태로 저장할 것이다.
dataX = []
dataY = []
dataZ = []

# 행성에 대한 정보 입력 받기
for i in range(1, N + 1):
    x, y, z = list(map(int, input().split()))
    dataX.append((x, i))
    dataY.append((y, i))
    dataZ.append((z, i))

# 좌표대로 정렬
dataX.sort()
dataY.sort()
dataZ.sort()

edges = []

def formattedEdge(nextData, currentData):
    nextPoint, nextPlanetNumber = nextData
    currentPoint, currentPlanetNumber = currentData
    return (nextPoint - currentPoint, currentPlanetNumber, nextPlanetNumber)

# 인접한 노드들로부터 간선 정보를 추출하여 처리
for i in range(N - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append(formattedEdge(dataX[i + 1], dataX[i]))
    edges.append(formattedEdge(dataY[i + 1], dataY[i]))
    edges.append(formattedEdge(dataZ[i + 1], dataZ[i]))

# 간선을 비용순으로 정렬
edges.sort()

total = 0
for cost, a, b in edges:
    # 같은 행성일 때는 확인할 필요가 없으므로 a != b 조건문을 추가
    if a != b and find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost

print(total)