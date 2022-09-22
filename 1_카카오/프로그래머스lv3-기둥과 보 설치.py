# 이코테 풀이
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

# 나의 풀이
def solution(n, build_frame):
    pillars = [[False] * (n + 1) for _ in range(n + 1)]
    beams = [[False] * (n + 1) for _ in range(n + 1)]
    
    def is_possible_pillar(x, y):
        # 바닥에 설치하는 경우
        if y == 0:
            return True
        # 보의 양 끝 위에 설치하는 경우
        if beams[x][y] or (x > 0 and beams[x - 1][y]):
            return True
        # 기둥 위에 설치하는 경우
        if (y > 0 and pillars[x][y - 1]):
            return True
        return False
    
    def is_possible_beam(x, y):
        # 기둥 위에 설치하는 경우
        if (y > 0 and pillars[x][y - 1]) or (y > 0 and x < n and pillars[x + 1][y - 1]):
            return True
        # 보 사이에 설치하는 경우
        if (x > 0 and beams[x - 1][y]) and (x < n and beams[x + 1][y]):
            return True
        return False
    
    def check_matrix():
        for x in range(n + 1):
            for y in range(n + 1):
                # 이 기둥이 불안정하다면
                if pillars[x][y] and not is_possible_pillar(x, y):
                    return False
                # 이 보가 불안정하다면
                if beams[x][y] and not is_possible_beam(x, y):
                    return False
        return True
    
    # 설치가 가능한지 확인하고 설치한다.
    def install(x, y, stuff):
        # 기둥이라면
        if stuff == 0:
            if is_possible_pillar(x, y):
                pillars[x][y] = True
                return True
        # 보라면
        else:
            if is_possible_beam(x, y):
                beams[x][y] = True
                return True
        return False
    
    # 일단 삭제했다가 모든 값을 순회하면서 조건에서 벗어난 기둥이나 보가 있는지 확인한다.
    # 조건에서 벗어났다면 삭제했던 것을 다시 설치
    def remove(x, y, stuff):
        if stuff == 0:
            pillars[x][y] = False
            if not check_matrix():
                pillars[x][y] = True
                return False
        else:
            beams[x][y] = False
            if not check_matrix():
                beams[x][y] = True
                return False
        return True
    
    
    result = []
    for x, y, stuff, command in build_frame:
        if command == 1:
            if install(x, y, stuff):
                result.append([x, y, stuff])
        else:
            if remove(x, y, stuff):
                result.remove([x, y, stuff])
    
    return sorted(result)
"""
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.1MB)
테스트 2 〉	통과 (0.18ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.1MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.42ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (12.46ms, 10.3MB)
테스트 11 〉	통과 (24.06ms, 10.4MB)
테스트 12 〉	통과 (51.52ms, 10.3MB)
테스트 13 〉	통과 (73.72ms, 10.7MB)
테스트 14 〉	통과 (12.71ms, 10.3MB)
테스트 15 〉	통과 (36.47ms, 10.5MB)
테스트 16 〉	통과 (50.22ms, 10.4MB)
테스트 17 〉	통과 (74.24ms, 10.5MB)
테스트 18 〉	통과 (242.30ms, 10.4MB)
테스트 19 〉	통과 (192.24ms, 10.6MB)
테스트 20 〉	통과 (178.00ms, 10.4MB)
테스트 21 〉	통과 (263.43ms, 10.4MB)
테스트 22 〉	통과 (300.17ms, 10.4MB)
테스트 23 〉	통과 (204.81ms, 10.5MB)
"""