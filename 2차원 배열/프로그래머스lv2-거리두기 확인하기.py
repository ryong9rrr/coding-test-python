# 가까이 앉아있는 사람들 리스트와 전체 리스트를 입력받아 결과를 반환합니다.
def check_mht(arr:list, matrix:list)->bool:
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            [m1, n1] = arr[i]
            [m2, n2] = arr[j]
            # 맨해튼거리가
            distance = abs(m2-m1) + abs(n2-n1)
            # 1이라면 거리두기를 지키지 않은 것입니다.
            if distance == 1:
                return 0
            # 2라면 파티션의 유무를 확인합니다.
            # 테이블만 놓여져 있다면 거리두기를 지키지 않은 것입니다.
            elif distance == 2:
                if m2 == m1 and matrix[m1][n2-1] == "O":
                    return 0
                elif n1 == n2 and matrix[m2-1][n1] == "O":
                    return 0
                else:
                    x = matrix[m1][n2]
                    y = matrix[m2][n1]
                    if x == "O" or y == "O":
                        return 0
    # 모두 확인을 해서 이상이 없다면 거리두기를 잘 지킨 것입니다.
    return 1

def solution(places):
    result = []
    for place in places:
        # 가까이 앉아있는 사람들을 찾습니다.
        close = []
        for m in range(5):
            for n in range(5):
                c = place[m][n]
                if c == "P":
                    close.append([m, n])
        # 거리를 확인하여 결과를 반환합니다.
        result.append(check_mht(close, place))
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.03ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.04ms, 10.3MB)
테스트 21 〉	통과 (0.03ms, 10.2MB)
테스트 22 〉	통과 (0.03ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
테스트 30 〉	통과 (0.02ms, 10.3MB)
"""

############################# 고생의 흔적... ##################################
# n x n 형태일때
n = 5
room = []
for j in range(n):
    temp = []
    for i in range(1, n + 1):
        temp.append(5*j+i)
    room.append(temp)

print(room)
"""
[[1, 2, 3, 4, 5], 
 [6, 7, 8, 9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25]]
"""

# 아래 좌표를 기준으로 분할
a = [1, 1]
b = [1, 3]
c = [3, 1]
d = [3, 3]

def divide(coordinate:list, matrix:list)->list:
    result = []
    [m, n] = coordinate
    for i in range(-1, 2):
        result.append(matrix[m+i][n-1:n+2])
    return result

print(divide(a, room))
print(divide(b, room))
print(divide(c, room))
print(divide(d, room))
"""
[[1, 2, 3], [6, 7, 8], [11, 12, 13]]
[[3, 4, 5], [8, 9, 10], [13, 14, 15]]
[[11, 12, 13], [16, 17, 18], [21, 22, 23]]
[[13, 14, 15], [18, 19, 20], [23, 24, 25]]
"""

s = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]

print(divide(a, s))
"""
['POO', 'OXX', 'OPX']
"""