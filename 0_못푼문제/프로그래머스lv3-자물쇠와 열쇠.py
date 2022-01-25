# 이코테 풀이
def rotate_matrix_90(matrix:list)->list:
    n, m = len(matrix), len(matrix[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_matrix_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                if check(new_lock):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

"""
정확성  테스트
테스트 1 〉	통과 (0.68ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (12.39ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (34.02ms, 10.3MB)
테스트 6 〉	통과 (30.79ms, 10.3MB)
테스트 7 〉	통과 (285.02ms, 10.3MB)
테스트 8 〉	통과 (64.34ms, 10.3MB)
테스트 9 〉	통과 (100.24ms, 10.3MB)
테스트 10 〉	통과 (187.01ms, 10.3MB)
테스트 11 〉	통과 (374.33ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (7.05ms, 10.3MB)
테스트 14 〉	통과 (0.97ms, 10.3MB)
테스트 15 〉	통과 (8.20ms, 10.3MB)
테스트 16 〉	통과 (38.14ms, 10.3MB)
테스트 17 〉	통과 (102.48ms, 10.3MB)
테스트 18 〉	통과 (42.31ms, 10.3MB)
테스트 19 〉	통과 (0.93ms, 10.3MB)
테스트 20 〉	통과 (141.37ms, 10.3MB)
테스트 21 〉	통과 (244.31ms, 10.3MB)
테스트 22 〉	통과 (28.37ms, 10.3MB)
테스트 23 〉	통과 (5.40ms, 10.3MB)
테스트 24 〉	통과 (5.89ms, 10.3MB)
테스트 25 〉	통과 (259.76ms, 10.3MB)
테스트 26 〉	통과 (285.79ms, 10.3MB)
테스트 27 〉	통과 (485.75ms, 10.3MB)
테스트 28 〉	통과 (29.95ms, 10.4MB)
테스트 29 〉	통과 (9.78ms, 10.3MB)
테스트 30 〉	통과 (45.14ms, 10.4MB)
테스트 31 〉	통과 (132.48ms, 10.3MB)
테스트 32 〉	통과 (278.16ms, 10.3MB)
테스트 33 〉	통과 (45.37ms, 10.3MB)
테스트 34 〉	통과 (2.96ms, 10.3MB)
테스트 35 〉	통과 (2.55ms, 10.3MB)
테스트 36 〉	통과 (4.61ms, 10.3MB)
테스트 37 〉	통과 (2.59ms, 10.3MB)
테스트 38 〉	통과 (0.91ms, 10.3MB)
"""