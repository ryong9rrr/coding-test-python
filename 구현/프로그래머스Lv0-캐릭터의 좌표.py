def solution(keyinput, board):
    limit_x = (board[0] - 1) // 2
    limit_y = (board[1] - 1) // 2

    commands = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0],
    }
    
    x = y = 0
    for command in keyinput:
        dx, dy = commands[command]
        nx, ny = x + dx, y + dy
        if abs(nx) <= limit_x and abs(ny) <= limit_y:
            x, y = nx, ny
    
    return [x, y]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
"""