def fill_matrix(head_x, head_y, number, width, matrix):
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    x = head_x
    y = head_y
    
    matrix[x][y] = number
    number += 1
    
    def fill_and_move(direction):
        nonlocal x
        nonlocal y
        nonlocal number
        x += dx[direction]
        y += dy[direction]
        matrix[x][y] = number
        number += 1
    
    for _ in range(width - 1):
        fill_and_move(0)
        
    for _ in range(width - 1):
        fill_and_move(1)
        
    for _ in range(width - 2):
        fill_and_move(2)
        
    return number

def solution(n):
    matrix = [[0] * n for _ in range(n)]

    number = 1
    head_x = head_y = 0
    width = n
    while width >= 1:
        number = fill_matrix(head_x, head_y, number, width, matrix)
        head_x += 2
        head_y += 1
        width -= 3
    
    result = []
    for i in range(n):
        for j in range(i + 1):
            result.append(matrix[i][j])
                
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (1.58ms, 10.5MB)
테스트 5 〉	통과 (1.57ms, 10.5MB)
테스트 6 〉	통과 (1.57ms, 10.5MB)
테스트 7 〉	통과 (342.89ms, 42.1MB)
테스트 8 〉	통과 (342.19ms, 42.1MB)
테스트 9 〉	통과 (184.38ms, 42.2MB)
"""