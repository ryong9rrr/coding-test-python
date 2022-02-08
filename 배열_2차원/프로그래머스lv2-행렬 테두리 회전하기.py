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

"""js
function initMatrix(rows, columns){
    const matrix = [];
    let i = 1;
    for (let x = 0; x < rows; x++){
        const row = []
        for (let y = 0; y < columns; y++){
            row.push(i++)
        }
        matrix.push(row)
    }
    return matrix
}

function getEdges(n1, m1, n2, m2){
    const q = [];
    for (let j = m1; j < m2 + 1; j++){
        q.push([n1, j])
    }
    for (let i = n1 + 1; i < n2 + 1; i++){
        q.push([i, m2])
    }
    for (let j = m2 - 1; j > m1 - 1; j--){
        q.push([n2, j])
    }
    for (let i = n2 - 1; i > n1; i--){
        q.push([i, m1])
    }
    return q
}

function solution(rows, columns, queries) {
    const matrix = initMatrix(rows, columns)
    const result = []
    
    for (const [n1, m1, n2, m2] of queries){
        const q = getEdges(n1, m1, n2, m2)
        const rot_q = [...q]
        rot_q.push(rot_q.shift())
        
        const prev = []
        for (const [prevX, prevY] of q){
            prev.push(matrix[prevX - 1][prevY - 1])
        }
        result.push(Math.min(...prev))
        for (let i = 0; i < prev.length; i++){
            const prevValue = prev[i]
            const [nextX, nextY] = rot_q[i]
            matrix[nextX - 1][nextY - 1] = prevValue
        }
    }
    return result
}

정확성  테스트
테스트 1 〉	통과 (0.40ms, 30.4MB)
테스트 2 〉	통과 (0.23ms, 30.1MB)
테스트 3 〉	통과 (58.07ms, 41.5MB)
테스트 4 〉	통과 (42.26ms, 38.1MB)
테스트 5 〉	통과 (81.25ms, 41.4MB)
테스트 6 〉	통과 (51.01ms, 41.4MB)
테스트 7 〉	통과 (79.03ms, 41.5MB)
테스트 8 〉	통과 (61.11ms, 38.4MB)
테스트 9 〉	통과 (53.52ms, 41.8MB)
테스트 10 〉	통과 (70.96ms, 41.2MB)
테스트 11 〉	통과 (55.70ms, 41.1MB)
"""