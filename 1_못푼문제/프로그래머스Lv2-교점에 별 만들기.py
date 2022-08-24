# 두 직선 A, B의 교점 (Px, Py)를 구하는 함수
# A = B = [number, number, number]
# 직선이 평행하거나 일치한다면 None을 리턴한다.
def intersection_point(A, B):
    a1, b1, c1 = A
    a2, b2, c2 = B
    numerator = (b1 * c2) - (b2 * c1)
    denominator = (a1 * b2) - (a2 * b1)
    if denominator == 0:
        return None
    Px = numerator / denominator
    Py = ((-1 * (a1 / b1)) * Px) - (c1 / b1)
    return [Px, Py]

def solution(line):
    N = len(line)
    POINTS = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            points = intersection_point(line[i], line[j])
            if points:
                a, b = points
                if a == int(a) and b == int(b):
                    POINTS.append([int(a), int(b)])
    
    minX = minY = int(1e9)
    maxX = maxY = 0

    for x, y in POINTS:
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
    
    rangeX = maxX - minX + 1
    rangeY = maxY - minY + 1

    matrix = [["."] * rangeX for _ in range(rangeY)]
    
    for x, y in POINTS:
        cx = x - minX
        cy = y - minY
        matrix[cy][cx] = "*"
    
    matrix.reverse()

    return ["".join(row) for row in matrix]
"""
정확성 테스트
테스트 1 〉 실패 (0.09ms, 10.4MB)
테스트 2 〉 통과 (3.82ms, 12.2MB)
테스트 3 〉 실패 (런타임 에러)
테스트 4 〉 통과 (7.49ms, 14.6MB)
테스트 5 〉 실패 (런타임 에러)
테스트 6 〉 실패 (런타임 에러)
테스트 7 〉 통과 (3.09ms, 12MB)
테스트 8 〉 통과 (0.05ms, 10.3MB)
테스트 9 〉 통과 (182.04ms, 10.5MB)
테스트 10 〉 통과 (193.42ms, 10.4MB)
테스트 11 〉 실패 (런타임 에러)
테스트 12 〉 실패 (279.27ms, 10.4MB)
테스트 13 〉 실패 (런타임 에러)
테스트 14 〉 실패 (311.77ms, 10.3MB)
테스트 15 〉 실패 (런타임 에러)
테스트 16 〉 통과 (286.40ms, 10.3MB)
테스트 17 〉 실패 (306.87ms, 10.3MB)
테스트 18 〉 통과 (241.80ms, 11.1MB)
테스트 19 〉 통과 (243.45ms, 10.4MB)
테스트 20 〉 통과 (213.57ms, 10.4MB)
테스트 21 〉 통과 (205.37ms, 12MB)
테스트 22 〉 실패 (0.95ms, 10.5MB)
테스트 23 〉 실패 (29.61ms, 18.3MB)
테스트 24 〉 실패 (10.75ms, 14MB)
테스트 25 〉 실패 (1.03ms, 10.4MB)
테스트 26 〉 실패 (0.15ms, 10.4MB)
테스트 27 〉 실패 (런타임 에러)
테스트 28 〉 실패 (런타임 에러)
테스트 29 〉 통과 (0.02ms, 10.3MB)
"""

# 두번째 시도...

# 두 직선 A, B의 교점 (Px, Py)를 구하는 함수
# A = B = [number, number, number]
# 직선이 평행하거나 일치한다면 None을 리턴한다.
def intersection_point(A, B):
    a1, b1, c1 = A
    a2, b2, c2 = B
    numerator = (b1 * c2) - (b2 * c1)
    denominator = (a1 * b2) - (a2 * b1)
    if denominator == 0:
        return None
    Px = numerator / denominator
    Py = ((-1 * (a1 / b1)) * Px) - (c1 / b1)
    return [Px, Py]

def solution(line):
    N = len(line)
    POINTS = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            points = intersection_point(line[i], line[j])
            if points:
                a, b = points
                if a == int(a) and b == int(b):
                    POINTS.append([int(a), int(b)])
    
    minX = minY = int(1e9)
    maxX = maxY = 0

    for x, y in POINTS:
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)
    
    rangeX = maxX - minX + 1
    rangeY = maxY - minY + 1

    matrix = [["."] * rangeX for _ in range(rangeY)]
    
    for x, y in POINTS:
        cx = x - minX
        cy = maxY - y
        #print(x, y, "->", cx, cy)
        matrix[cy][cx] = "*"

    # for row in matrix:
    #     print(row)

    return ["".join(row) for row in matrix]
"""
정확성 테스트
테스트 1 〉 실패 (0.17ms, 10.2MB)
테스트 2 〉 통과 (6.17ms, 12.3MB)
테스트 3 〉 실패 (런타임 에러)
테스트 4 〉 통과 (7.93ms, 14.5MB)
테스트 5 〉 실패 (런타임 에러)
테스트 6 〉 실패 (런타임 에러)
테스트 7 〉 통과 (3.60ms, 12MB)
테스트 8 〉 통과 (0.09ms, 10.2MB)
테스트 9 〉 통과 (204.66ms, 10.6MB)
테스트 10 〉 통과 (278.24ms, 10.6MB)
테스트 11 〉 실패 (런타임 에러)
테스트 12 〉 실패 (315.99ms, 10.5MB)
테스트 13 〉 실패 (런타임 에러)
테스트 14 〉 실패 (246.69ms, 10.3MB)
테스트 15 〉 실패 (런타임 에러)
테스트 16 〉 통과 (254.05ms, 10.3MB)
테스트 17 〉 실패 (271.03ms, 10.5MB)
테스트 18 〉 통과 (334.29ms, 11MB)
테스트 19 〉 통과 (265.57ms, 10.2MB)
테스트 20 〉 통과 (269.17ms, 10.2MB)
테스트 21 〉 통과 (274.65ms, 11.8MB)
테스트 22 〉 실패 (0.71ms, 10.3MB)
테스트 23 〉 실패 (29.70ms, 18.3MB)
테스트 24 〉 실패 (11.93ms, 14MB)
테스트 25 〉 실패 (1.00ms, 10.3MB)
테스트 26 〉 실패 (0.16ms, 10.4MB)
테스트 27 〉 실패 (런타임 에러)
테스트 28 〉 실패 (런타임 에러)
테스트 29 〉 통과 (0.02ms, 10MB)
"""