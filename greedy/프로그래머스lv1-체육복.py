from collections import defaultdict
def solution(n, lost, reserve):
    result = n - len(lost)
    
    students = defaultdict(int)
    
    for i in range(1, n + 1):
        students[i] = 1
    
    for i in lost:
        students[i] -= 1
    
    for i in reserve:
        students[i] += 1
        
    for i in range(1, n + 1):
        if students[i] == 0:
            if students[i - 1] >= 2:
                students[i] += 1
                students[i - 1] -= 1
            elif students[i + 1] >= 2:
                students[i] += 1
                students[i + 1] -= 1
    result = 0
    for i in range(1, n + 1):
        if students[i] >= 1:
            result += 1
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
"""


# 더 깔끔한 풀이
from collections import defaultdict
def solution(n, lost, reserve):
    # {학생번호:가지고 있는 체육복의 수}
    students = defaultdict(int)
    for i in range(1, n + 1):
        # 모든학생은 한벌을 가지고 있었다고 가정
        students[i] = 1
        # 잃어버린 학생은 -1
        if i in lost:
            students[i] -= 1
        # 여벌이 있는 학생은 +1
        if i in reserve:
            students[i] += 1
    
    for i in range(1, n + 1):
        # 체육복이 없는 학생이 있다면
        if not students[i]:
            # defaultdict를 사용했기 때문에 i 크기에 대한 방어코드는 없어도 되긴 함
            # 앞에 사람이 여벌이 있다면 체육복 빌리기
            if i > 1 and students[i - 1] == 2:
                students[i - 1] -= 1
                students[i] += 1
            # 뒤에 사람이 여벌이 있다면 체육복 빌리기
            elif i < n + 1 and students[i + 1] == 2:
                students[i + 1] -= 1
                students[i] += 1
    # 체육복이 있는 사람만 count
    count = 0
    for i in range(1, n + 1):
        if students[i]:
            count += 1
    return count

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.4MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
"""