# 행렬을 직접적으로 넘겨주는 방법 (내 방법)
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))

# 원소들의 전체 합을 리턴하는 함수
def checkSum(mat):
    _sum = 0
    for row in mat:
        _sum += sum(row)
    return _sum

# 결과값을 담을 전역변수
result = ""
def divide(mat:list, n):
    global result
    # 행렬이 1 x 1 형태가 되면 그 값을 리턴한다.
    if n == 1:
        result += str(mat[0][0])
        return

    _sum = checkSum(mat)
    # 합이 크기와 같다면 모두 1로 구성되어있는 것
    if _sum == n ** 2:
        result += "1"
        return
    # 합이 0이라면 모두 0으로 구성되어있는 것
    elif _sum == 0:
        result += "0"
        return
    # 그렇지 않다면 4분할
    else:
        result += "("
        mid = len(mat) // 2
        divide([row[:mid] for row in mat[:mid]], mid)
        divide([row[mid:] for row in mat[:mid]], mid)
        divide([row[:mid] for row in mat[mid:]], mid)
        divide([row[mid:] for row in mat[mid:]], mid)
        result += ")"

divide(matrix, n)

print(result)

################################################################

# 재귀의 진수를 보여주는 우아한 풀이...
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input())

def divide(n, i, j):
    if n == 1:
        return matrix[i][j]
    mid = n // 2
    a = divide(mid, i, j)
    b = divide(mid, i, j + mid)
    c = divide(mid, i + mid, j)
    d = divide(mid, i + mid, j + mid)
    if a == b and b == c and c == d and len(a) == 1:
        return a
    else:
        return "(" + a + b + c + d + ")"

print(divide(n, 0, 0))