# N x N 행렬을 오른쪽으로 90도 회전하는 함수
def rotate_matrix_90(matrix):
    N = len(matrix)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - i - 1] = matrix[i][j]
    return result

def solution(key, lock):
    len_lock = len(lock)
    len_key = len(key)
    extended_side = len_key - 1
    extended_range = extended_side * 2 + len_lock
    
    # 확장된 행렬 만들기
    extended_matrix = [[0] * extended_range for _ in range(extended_range)]
    for i in range(len_lock):
        for j in range(len_lock):
            x = i + extended_side
            y = j + extended_side
            extended_matrix[x][y] = lock[i][j]
    
    # 확장된 행렬에서 lock 부분을 체크하는 함수.
    # 모두 1일 때 딱 맞춰진 상태가 된다.
    def check_lock():
        for x in range(len_lock):
            for y in range(len_lock):
                if extended_matrix[x + extended_side][y + extended_side] != 1:
                    return False
        return True
    
    # 완전탐색
    for _ in range(4):
        key = rotate_matrix_90(key)
        for x in range(extended_side + len_lock):
            for y in range(extended_side + len_lock):
                # key를 넣어본다.
                for i in range(len_key):
                    for j in range(len_key):
                        extended_matrix[x + i][y + j] += key[i][j]
                # 넣은 상태로 자물쇠 확인
                if check_lock():
                    return True
                # key를 다시 뺀다
                for i in range(len_key):
                    for j in range(len_key):
                        extended_matrix[x + i][y + j] -= key[i][j]
    return False
"""
정확성  테스트
테스트 1 〉	통과 (0.51ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (8.66ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.4MB)
테스트 5 〉	통과 (23.21ms, 10.2MB)
테스트 6 〉	통과 (12.93ms, 10.2MB)
테스트 7 〉	통과 (124.50ms, 10.2MB)
테스트 8 〉	통과 (56.67ms, 10.3MB)
테스트 9 〉	통과 (73.64ms, 10.1MB)
테스트 10 〉	통과 (186.70ms, 10.2MB)
테스트 11 〉	통과 (333.45ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (3.13ms, 10.2MB)
테스트 14 〉	통과 (0.57ms, 10.2MB)
테스트 15 〉	통과 (6.26ms, 10.3MB)
테스트 16 〉	통과 (33.09ms, 10.3MB)
테스트 17 〉	통과 (85.52ms, 10.2MB)
테스트 18 〉	통과 (14.66ms, 10.2MB)
테스트 19 〉	통과 (0.66ms, 10.3MB)
테스트 20 〉	통과 (117.70ms, 10.2MB)
테스트 21 〉	통과 (153.62ms, 10.1MB)
테스트 22 〉	통과 (30.86ms, 10.1MB)
테스트 23 〉	통과 (4.03ms, 10.3MB)
테스트 24 〉	통과 (4.23ms, 10.4MB)
테스트 25 〉	통과 (164.94ms, 10.4MB)
테스트 26 〉	통과 (313.54ms, 10.2MB)
테스트 27 〉	통과 (530.49ms, 10.3MB)
테스트 28 〉	통과 (33.29ms, 10.3MB)
테스트 29 〉	통과 (8.19ms, 10.2MB)
테스트 30 〉	통과 (44.02ms, 10.4MB)
테스트 31 〉	통과 (67.83ms, 10.3MB)
테스트 32 〉	통과 (189.88ms, 10.2MB)
테스트 33 〉	통과 (45.00ms, 10MB)
테스트 34 〉	통과 (4.53ms, 10.1MB)
테스트 35 〉	통과 (3.89ms, 10.3MB)
테스트 36 〉	통과 (4.24ms, 10.1MB)
테스트 37 〉	통과 (2.46ms, 10.3MB)
테스트 38 〉	통과 (0.65ms, 10.1MB)
"""