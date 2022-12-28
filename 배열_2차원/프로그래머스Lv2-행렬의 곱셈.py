def multiplyMatrix(matrix1, matrix2):
    def multiply(arr1, arr2):
        result = 0
        for i, v in enumerate(arr1):
            result = result + v * arr2[i]
        return result
    
    def getColumns(matrix, j):
        result = []
        for i in range(len(matrix)):
            result.append(matrix[i][j])
        return result
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(multiply(matrix1[i], getColumns(matrix2, j)))
        result.append(row)
    return result

def solution(arr1, arr2):
    return multiplyMatrix(arr1, arr2)

"""
정확성  테스트
테스트 1 〉	통과 (3.99ms, 10.4MB)
테스트 2 〉	통과 (86.43ms, 10.8MB)
테스트 3 〉	통과 (150.03ms, 11.2MB)
테스트 4 〉	통과 (1.89ms, 10.2MB)
테스트 5 〉	통과 (62.22ms, 10.9MB)
테스트 6 〉	통과 (44.28ms, 11MB)
테스트 7 〉	통과 (3.18ms, 10.2MB)
테스트 8 〉	통과 (1.45ms, 10.1MB)
테스트 9 〉	통과 (0.67ms, 10.2MB)
테스트 10 〉	통과 (80.40ms, 10.5MB)
테스트 11 〉	통과 (10.24ms, 10.3MB)
테스트 12 〉	통과 (1.18ms, 10.2MB)
테스트 13 〉	통과 (69.22ms, 10.7MB)
테스트 14 〉	통과 (89.56ms, 10.8MB)
테스트 15 〉	통과 (37.25ms, 10.6MB)
테스트 16 〉	통과 (10.82ms, 10.7MB)
"""

# zip 사용
def solution(X, Y):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer
"""
정확성  테스트
테스트 1 〉	통과 (2.04ms, 10.4MB)
테스트 2 〉	통과 (40.14ms, 11MB)
테스트 3 〉	통과 (41.52ms, 11.2MB)
테스트 4 〉	통과 (1.79ms, 10.4MB)
테스트 5 〉	통과 (27.79ms, 10.9MB)
테스트 6 〉	통과 (16.63ms, 10.9MB)
테스트 7 〉	통과 (1.46ms, 10.3MB)
테스트 8 〉	통과 (0.62ms, 10.3MB)
테스트 9 〉	통과 (0.38ms, 10.3MB)
테스트 10 〉	통과 (27.72ms, 10.7MB)
테스트 11 〉	통과 (2.84ms, 10.4MB)
테스트 12 〉	통과 (0.92ms, 10.3MB)
테스트 13 〉	통과 (20.72ms, 10.8MB)
테스트 14 〉	통과 (44.35ms, 10.9MB)
테스트 15 〉	통과 (13.24ms, 10.5MB)
테스트 16 〉	통과 (9.09ms, 10.7MB)
"""