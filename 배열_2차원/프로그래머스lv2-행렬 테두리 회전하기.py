# 큐 / 원형 큐 사용
import copy
from collections import deque
def init_matrix(rows, columns):
    matrix = []
    i = 1
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(i)
            i += 1
        matrix.append(row)
    return matrix

def get_edges(n1, m1, n2, m2):
    cq = deque()
    #top
    for j in range(m1, m2 + 1):
        cq.append([n1, j])
    #right
    for i in range(n1 + 1, n2 + 1):
        cq.append([i, m2])
    #bottom
    for j in range(m2 - 1, m1 - 1, -1):
        cq.append([n2, j])
    #left
    for i in range(n2 - 1, n1, -1):
        cq.append([i, m1])
    return cq

def solution(rows, columns, queries):
    matrix = init_matrix(rows, columns)
    result = []
    for n1, m1, n2, m2 in queries:
        cq = get_edges(n1, m1, n2, m2)
        rot_cq = copy.copy(cq) # 참조가 일어나므로 복사
        rot_cq.rotate(-1) # rot_cq.append(rot_cq.popleft())
        prev = []
        for prev_x, prev_y in cq:
            prev.append(matrix[prev_x - 1][prev_y - 1])
        result.append(min(prev))
        for i in range(len(prev)):
            prev_v = prev[i]
            next_x, next_y = rot_cq[i]
            matrix[next_x - 1][next_y - 1] = prev_v
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (291.35ms, 12.1MB)
테스트 4 〉	통과 (166.48ms, 11.4MB)
테스트 5 〉	통과 (220.10ms, 11.7MB)
테스트 6 〉	통과 (238.19ms, 12.3MB)
테스트 7 〉	통과 (266.75ms, 12.4MB)
테스트 8 〉	통과 (152.15ms, 11.5MB)
테스트 9 〉	통과 (233.97ms, 12.2MB)
테스트 10 〉	통과 (180.68ms, 11.8MB)
테스트 11 〉	통과 (168.08ms, 11.6MB)
"""

# 방식만 약간다를 뿐 거의 동일한 풀이
import copy
from collections import deque

# params: 좌측상단 좌표, 우측하단 좌표, 오른쪽으로 n칸 rotate
# returns: 이전 좌표의 배열, 이동된 좌표의 배열
def rotate(a, b, n):
    x1, y1 = a
    x2, y2 = b
    cq = deque()
    for y in range(y1, y2):
        cq.append([x1, y])
    for x in range(x1, x2):
        cq.append([x, y2])
    for y in range(y2, y1, -1):
        cq.append([x2, y])
    for x in range(x2, x1, -1):
        cq.append([x, y1])
        
    prev_q = copy.copy(cq)
    cq.rotate(n)
    return prev_q, cq

def solution(rows, columns, queries):
    # 행렬 초기화
    matrix = []
    i = 1
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(i)
            i += 1
        matrix.append(row)

    result = []
    for x1, y1, x2, y2 in queries:
        prevs, nexts = rotate([x1 - 1, y1 - 1], [x2 - 1, y2 - 1], 1)
        next_values = [matrix[x][y] for x, y in nexts]
        
        # 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자를 push
        result.append(min(next_values))

        for i in range(len(next_values)):
            x, y = prevs[i]
            matrix[x][y] = next_values[i]
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (227.83ms, 11.8MB)
테스트 4 〉	통과 (136.89ms, 11.3MB)
테스트 5 〉	통과 (201.94ms, 11.4MB)
테스트 6 〉	통과 (193.34ms, 11.9MB)
테스트 7 〉	통과 (213.26ms, 12.3MB)
테스트 8 〉	통과 (134.62ms, 11.5MB)
테스트 9 〉	통과 (200.64ms, 11.9MB)
테스트 10 〉	통과 (182.48ms, 11.4MB)
테스트 11 〉	통과 (142.08ms, 11.4MB)

"""