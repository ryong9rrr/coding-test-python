# N x N 행렬을 오른쪽으로 90도 회전하는 함수
def rotate_matrix_90(matrix):
    N = len(matrix)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - i - 1] = matrix[i][j]
    return result