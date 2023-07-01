# N x N 행렬을 오른쪽으로 90도 회전하는 함수
def rotate_matrix_90(matrix):
    N = len(matrix)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - i - 1] = matrix[i][j]
    return result


# 곱셈이 가능한 두 행렬 곱하기
def multiplyMatrix(matrix1, matrix2):
    def multiply(arr1, arr2):
        value = 0
        for i, v in enumerate(arr1):
            value = value + v * arr2[i]
        return value

    def get_columns(matrix, j):
        columns = []
        for i in range(len(matrix)):
            columns.append(matrix[i][j])
        return columns

    multiplied_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(multiply(matrix1[i], get_columns(matrix2, j)))
        multiplied_matrix.append(row)
    return multiplied_matrix
