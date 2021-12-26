n = 3
matrix = [[0] * n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        matrix[i][j] = num
        num += 1

print(matrix)
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

def rotate_matrix_90(matrix:list)->list:
    n, m = len(matrix), len(matrix[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result

print(rotate_matrix_90(matrix))
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]