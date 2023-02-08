# 파이썬 알고리즘 인터뷰 풀이
def solution(m, n, board):
    board = [list(x) for x in board]

    matched = True
    while matched:
        # 1) 일치 여부 판별
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == \
                        board[i][j + 1] == \
                        board[i + 1][j + 1] == \
                        board[i + 1][j] != '#':
                    matched.append([i, j])

        # 2) 일치한 위치 삭제
        for i, j in matched:
            board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = board[i + 1][j] = '#'

        # 3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'

    return sum(x.count('#') for x in board)
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (10.54ms, 10.2MB)
테스트 5 〉	통과 (1170.90ms, 10.4MB)
테스트 6 〉	통과 (79.92ms, 10.1MB)
테스트 7 〉	통과 (7.34ms, 10.3MB)
테스트 8 〉	통과 (12.48ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (7.08ms, 10.2MB)
테스트 11 〉	통과 (27.02ms, 10.1MB)
"""

# 행렬을 90도 회전해서 rearrange를 더 용이하게 함, 불필요하게 3중 루프를 사용할 필요가 없음.
def rotate_board(board):
    result = []
    for j in range(len(board[0])):
        row = []
        for i in range(len(board) - 1, -1, -1):
            row.append(board[i][j])
        result.append(row)
    return result

def solution(m, n, board):
    matrix = rotate_board(board)
    
    def search():
        result = []
        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1] != "#":
                    result.append((i, j))
        return result
    
    def remove(targets):
        for i, j in targets:
            matrix[i][j] = matrix[i][j + 1] = matrix[i + 1][j] = matrix[i + 1][j + 1] = "#"
            
    def rearrange():
        for i in range(n):
            matrix[i] = [x for x in matrix[i] if x != "#"]
            matrix[i] = matrix[i] + (["#"] * (m - len(matrix[i])))
    
    while True:
        targets = search()
        
        if not targets:
            return sum([row.count("#") for row in matrix])
        
        remove(targets)
        rearrange()

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.81ms, 10.2MB)
테스트 5 〉	통과 (80.57ms, 10.4MB)
테스트 6 〉	통과 (3.52ms, 10.2MB)
테스트 7 〉	통과 (0.46ms, 10.2MB)
테스트 8 〉	통과 (1.54ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.67ms, 10.1MB)
테스트 11 〉	통과 (1.40ms, 10.2MB)
"""