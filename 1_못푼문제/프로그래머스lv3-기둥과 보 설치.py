def solution(n, build_frame):
    # _type은 1또는 2, 1은 기둥, 2는 보
    table = [[0] * (n + 1) for _ in range(n + 1)]
    
    def is_possible_pillar(x, y):
        if y == 0:
            return True
        if table[x][y - 1] == 1:
            return True
        if table[x - 1][y] == 2 or table[x][y] == 2:
            return True
        return False
    
    def is_possible_beam(x, y):
        if table[x][y - 1] == 1:
            return True
        if table[x + 1][y - 1] == 1:
            return True
        if table[x - 1][y] == 2 and table[x + 1][y] == 2:
            return True
        return False
    
    for x, y, _type, command in build_frame:
        # 설치 명령이라면
        if command == 1:
            # 기둥을 설치할 수 있다면
            if _type == 0 and is_possible_pillar(x, y):
                table[x][y] = 1
            # 보를 설치할 수 있다면
            if _type == 1 and is_possible_beam(x, y):
                table[x][y] = 2
        # 삭제 명령이라면
        if command == 0:
            # 기둥이라면
            if _type == 0:
                # 바로 위에 보가 있다면
                if table[x][y + 1] == 2:
                    # 일단 삭제해본다.
                    table[x][y] = 0
                    # 기둥을 삭제했을 때 보가 안전하지 않다면 다시 복구
                    if not is_possible_beam(x, y + 1):
                        table[x][y] = 1
                else:
                    # 보가 없다면 그 옆에 보가 있는지 확인
                    if table[x - 1][y] == 2:
                        # 일단 삭제해본다.
                        table[x][y] = 0
                        # 기둥을 삭제했을 때 보가 안전하지 않다면 다시 복구
                        if not is_possible_beam(x - 1, y):
                            table[x][y] = 1
                    else:
                        # 그 옆에 보가 없다면 삭제 가능
                        table[x][y] = 0
            # 보라면
            if _type == 1:
                # 적어도 한쪽 끝에 기둥이 있다면 삭제 가능
                if table[x - 1][y] == 1 or table[x + 1][y - 1] == 1:
                    table[x][y] = 0
        
    result = []
    for i in range(n + 1):
        for j in range(n + 1):
            value = table[i][j]
            if value != 0:
                result.append([i, j, value - 1])
    
    return sorted(result)
"""
정확성  테스트
테스트 1 〉	실패 (0.03ms, 10.4MB)
테스트 2 〉	실패 (0.03ms, 10.3MB)
테스트 3 〉	실패 (0.03ms, 10.3MB)
테스트 4 〉	실패 (0.05ms, 10.4MB)
테스트 5 〉	실패 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	실패 (0.02ms, 10.3MB)
테스트 9 〉	실패 (0.03ms, 10.3MB)
테스트 10 〉	실패 (0.36ms, 10.5MB)
테스트 11 〉	실패 (0.55ms, 10.4MB)
테스트 12 〉	실패 (0.81ms, 10.4MB)
테스트 13 〉	실패 (2.00ms, 10.5MB)
테스트 14 〉	실패 (0.40ms, 10.3MB)
테스트 15 〉	실패 (0.97ms, 10.4MB)
테스트 16 〉	실패 (0.81ms, 10.4MB)
테스트 17 〉	실패 (1.22ms, 10.6MB)
테스트 18 〉	실패 (0.97ms, 10.5MB)
테스트 19 〉	실패 (0.95ms, 10.4MB)
테스트 20 〉	실패 (1.06ms, 10.4MB)
테스트 21 〉	실패 (1.06ms, 10.5MB)
테스트 22 〉	실패 (0.97ms, 10.4MB)
테스트 23 〉	실패 (0.93ms, 10.5MB)
"""


def solution(n, build_frame):
    answer = []
    
    def possible():
        for x, y, stuff in answer:
            if stuff == 0 and (y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer):
                continue
            if stuff == 1 and ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                continue
            return False
        return True
    
    for x, y, stuff, command in build_frame:
        if command == 1:
            answer.append([x, y, stuff])
            if not possible():
                answer.remove([x, y, stuff])
        if command == 0:
            answer.remove([x, y, stuff])
            if not possible():
                answer.append([x, y, stuff])
    
    return sorted(answer)
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.13ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.29ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.2MB)
테스트 6 〉	통과 (0.46ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.06ms, 10.3MB)
테스트 10 〉	통과 (321.20ms, 10.3MB)
테스트 11 〉	통과 (1849.46ms, 10.5MB)
테스트 12 〉	통과 (198.08ms, 10.2MB)
테스트 13 〉	통과 (1890.39ms, 10.5MB)
테스트 14 〉	통과 (236.04ms, 10.3MB)
테스트 15 〉	통과 (2159.20ms, 10.5MB)
테스트 16 〉	통과 (211.46ms, 10.3MB)
테스트 17 〉	통과 (1898.22ms, 10.5MB)
테스트 18 〉	통과 (1269.41ms, 10.3MB)
테스트 19 〉	통과 (1272.29ms, 10.5MB)
테스트 20 〉	통과 (1366.39ms, 10.3MB)
테스트 21 〉	통과 (1524.63ms, 10.4MB)
테스트 22 〉	통과 (1152.18ms, 10.2MB)
테스트 23 〉	통과 (1349.39ms, 10.4MB)
"""



def solution(n, build_frame):
    pillars = [[False] * (n + 1) for _ in range(n + 1)]
    beams = [[False] * (n + 1) for _ in range(n + 1)]
    
    def install_pillar(x, y):
        if y == 0 or (y >= 1 and pillars[x][y - 1]) or (x >= 1 and beams[x - 1][y]) or beams[x][y]:
            pillars[x][y] = True
    
    def install_beam(x, y):
        if (y >= 1 and pillars[x][y - 1]) or (x + 1 < n and y >= 1 and pillars[x + 1][y - 1]) or ((x >= 1 and beams[x - 1][y]) and (x + 1 < n and beams[x + 1][y])):
            beams[x][y] = True
            
    def install(x, y, stuff):
        if stuff == 0:
            install_pillar(x, y)
        else:
            install_beam(x, y)
            
    def is_possible_remove(x, y):
        
    
    for x, y, stuff, command in build_frame:
        if command == 1:
            install(x, y, stuff)
    
    
    print(pillars)
    
    print(stuff)