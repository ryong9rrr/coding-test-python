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