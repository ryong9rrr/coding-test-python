def move(command, x, y):
    commands = {
        "U": [-1, 0],
        "L": [0, -1],
        "D": [1, 0],
        "R": [0, 1]
    }
    dx, dy = commands[command]
    nx = x + dx
    ny = y + dy
    if -5 <= nx <= 5 and -5 <= ny <= 5:
        return [nx, ny]
    return [x, y]

def solution(dirs):
    x = y = 0
    visited = set()
    
    for command in dirs:
        nx, ny = move(command, x, y)
        if x == nx and y == ny:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y)) # 되돌아가는 케이스도 추가해줘야한다
        x, y = nx, ny
    
    return len(visited) // 2
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (0.12ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.05ms, 10.2MB)
테스트 12 〉	통과 (0.09ms, 10.2MB)
테스트 13 〉	통과 (0.09ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (0.08ms, 10.1MB)
테스트 16 〉	통과 (0.36ms, 10.2MB)
테스트 17 〉	통과 (0.58ms, 10.2MB)
테스트 18 〉	통과 (0.39ms, 10.2MB)
테스트 19 〉	통과 (0.36ms, 10.3MB)
테스트 20 〉	통과 (0.37ms, 10.2MB)
"""