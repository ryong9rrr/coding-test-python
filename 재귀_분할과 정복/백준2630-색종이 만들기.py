import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력값을 받아 행렬 초기화
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 재귀적으로 행렬을 4분할 하는 함수
blue = white = 0
def divide(matrix, n):
    global white, blue
    # 전체 행렬 값을 구한다.
    _sum = 0
    for row in matrix:
        _sum += sum(row)
    # 전체 행렬 값이 행렬의 크기와 같다면 파란색 색종이 + 1
    if _sum == n ** 2:
        blue += 1
        return
    # 전체 행렬 값이 0이라면 하얀색 색종이 + 1
    elif _sum == 0:
        white += 1
        return
    # 그렇지 않다면 4분할, 재귀호출 -> "파이써닉한 분할 방법"
    else:
        mid = n // 2
        divide([row[:mid] for row in matrix[:mid]], mid)
        divide([row[mid:] for row in matrix[:mid]], mid)
        divide([row[:mid] for row in matrix[mid:]], mid)
        divide([row[mid:] for row in matrix[mid:]], mid)

# 재귀함수 호출
divide(matrix, n)

print(white, blue, sep="\n")