# 행렬 자체를 슬라이싱해서 행렬을 인자로 넘겨주어 행렬에 직접적으로 접근하는 방법
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
matrix = []
for _ in range(n):
    data = list(input().split())
    matrix.append(data)

result = {
    "-1": 0,
    "0": 0,
    "1": 0,
}

def checkMatrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[0][0] != mat[i][j]:
                return False
    return True

def divide(mat):
    global result
    # 길이가 1인지 검사하지 않으면 시간초과가 날 수 있음.
    if len(mat) == 1:
        result[mat[0][0]] += 1
        return
    if checkMatrix(mat):
        result[mat[0][0]] += 1
        return
    else:
        d = len(mat) // 3
        divide([row[:d] for row in mat[:d]])
        divide([row[d:2*d] for row in mat[:d]])
        divide([row[2*d:3*d] for row in mat[:d]])
        divide([row[:d] for row in mat[d:2*d]])
        divide([row[d:2*d] for row in mat[d:2*d]])
        divide([row[2*d:3*d] for row in mat[d:2*d]])
        divide([row[:d] for row in mat[2*d:3*d]])
        divide([row[d:2*d] for row in mat[2*d:3*d]])
        divide([row[2*d:3*d] for row in mat[2*d:3*d]])

divide(matrix)

for ans in result.values():
    print(ans)


####################################################################
# 첫번째 원소의 인덱스 값으로 행렬에 간접적으로 접근하는 방법
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
matrix = []
for _ in range(n):
    data = list(input().split())
    matrix.append(data)

result = {
    "-1": 0,
    "0": 0,
    "1": 0,
}

def checkMatrix(n, i, j):
    for x in range(i, i + n):
        for y in range(j, j + n):
            if matrix[i][j] != matrix[x][y]:
                return False
    return True

def divide(n, i, j):
    global result
    # 길이가 1인지 검사하는 코드가 없어도 통과하지만, 이 코드 하나만으로 2600ms가 걸림. (없으면 5500ms)
    if n == 1:
        result[matrix[i][j]] += 1
        return
    if checkMatrix(n, i, j):
        result[matrix[i][j]] += 1
        return
    else:
        n //= 3
        divide(n, i, j)
        divide(n, i, j + n)
        divide(n, i, j + 2 * n)
        divide(n, i + n, j)
        divide(n, i + n, j + n)
        divide(n, i + n, j + 2 * n)
        divide(n, i + 2 * n, j)
        divide(n, i + 2 * n, j + n)
        divide(n, i + 2 * n, j + 2 * n)

divide(n, 0, 0)

for ans in result.values():
    print(ans)